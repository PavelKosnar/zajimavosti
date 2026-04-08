#include <stdio.h>
#include <functional>
#include <algorithm>
#include <string.h>

#include "board.h"
#include "peripherals.h"
#include "pin_mux.h"
#include "clock_config.h"
#include "fsl_debug_console.h"
#include "fsl_gpio.h"
#include "fsl_port.h"
#include "fsl_mrt.h"

#include "mcxn-kit.h"
#include "i2c-lib.h"
#include "si4735-lib.h"

// **************************************************************************
// Configuration & Globals
// **************************************************************************

#define R 0b00000001
#define W 0b00000000
#define PCF8574_ADDRESS 0x40 // Base address for PCF8574 with A0,A1,A2 grounded

// Global state variables
int g_freq = 10140;          // Default: 101.40 MHz (Radiožurnál)
uint8_t g_volume = 40;       // Range 0-63
char g_ps_name[9] = "        ";  // RDS Program Service (8 chars)
char g_radio_text[65] = "";      // RDS Radiotext (up to 64 chars)

// Peripheral instances
DigitalOut g_led_stereo( P3_16 ); // Stereo detection LED
DigitalOut g_led_debug( P3_17 );

DigitalIn g_but_vol_up( P3_18 );
DigitalIn g_but_vol_down( P3_19 );
DigitalIn g_but_freq_up( P3_20 );
DigitalIn g_but_freq_down( P3_21 );

// **************************************************************************
// Task Functions
// **************************************************************************

// Task: Set volume using SET_PROPERTY (0x12)
void radio_set_volume(uint8_t vol) {
    if (vol > 63) vol = 63;
    i2c_start();
    i2c_output(SI4735_ADDRESS | W);
    i2c_output(0x12);          // SET_PROPERTY command
    i2c_output(0x00);
    i2c_output(0x40);          // RX_VOLUME property HI
    i2c_output(0x00);          // RX_VOLUME property LO
    i2c_output(0x00);          // Value HI
    i2c_output(vol);           // Value LO
    i2c_stop();
}

// Task: Tune radio station using FM_TUNE_FREQ (0x20)
void radio_tune(int freq) {
    i2c_start();
    i2c_output(SI4735_ADDRESS | W);
    i2c_output(0x20);          // FM_TUNE_FREQ
    i2c_output(0x00);
    i2c_output(freq >> 8);     // Freq High byte
    i2c_output(freq & 0xFF);   // Freq Low byte
    i2c_output(0x00);
    i2c_stop();
    delay_ms(100);             // Give the IC time to settle
}

// Task: Implement light bar on PCF8574 based on signal level
void update_signal_bar(uint8_t rssi) {
    // Map RSSI (~0-60) to 0-8 LEDs
    int level = rssi / 7; 
    if (level > 8) level = 8;
    
    uint8_t mask = 0;
    for (int i = 0; i < level; i++) {
        mask |= (1 << i);
    }
    
    i2c_start();
    i2c_output(PCF8574_ADDRESS | W);
    i2c_output(~mask); // Usually active low on these kits
    i2c_stop();
}

// Task: Display Station Name (PS) and Radiotext (RT)
void update_rds() {
    i2c_start();
    i2c_output(SI4735_ADDRESS | W);
    i2c_output(0x24); // FM_RDS_STATUS
    i2c_output(0x01); // Interrupt Clear
    
    i2c_start();
    i2c_output(SI4735_ADDRESS | R);
    uint8_t status = i2c_input(); i2c_ack();
    uint8_t fifo   = i2c_input(); i2c_ack();
    uint8_t blkA_h = i2c_input(); i2c_ack();
    uint8_t blkA_l = i2c_input(); i2c_ack();
    uint8_t blkB_h = i2c_input(); i2c_ack();
    uint8_t blkB_l = i2c_input(); i2c_ack();
    uint8_t blkC_h = i2c_input(); i2c_ack();
    uint8_t blkC_l = i2c_input(); i2c_ack();
    uint8_t blkD_h = i2c_input(); i2c_ack();
    uint8_t blkD_l = i2c_input(); i2c_nack(); 
    i2c_stop();

    // Group 0A parsing for Station Name (PS)
    if ((blkB_h & 0xF8) == 0x00) {
        int idx = (blkB_l & 0x03) * 2;
        g_ps_name[idx] = blkD_h;
        g_ps_name[idx+1] = blkD_l;
    }
}

// **************************************************************************
// Main Entry Point
// **************************************************************************

int main() {
    uint8_t l_RSSI, l_ST_status;
    uint8_t l_ack = 0;

    PRINTF("MCXN-KIT Initializing...\r\n");
    i2c_init();

    // Task: Initialize Si4735
    if ((l_ack = si4735_init()) != 0) {
        PRINTF("Radio init failed: %d\n", l_ack);
        return 0;
    }

    radio_tune(g_freq);
    radio_set_volume(g_volume);

    while (1) {
        // --- Input Tasks: Button Checks ---
        if (g_but_freq_up.read() == 0) {
            g_freq += 10;
            radio_tune(g_freq);
            memset(g_ps_name, ' ', 8); // Reset name on change
        }
        if (g_but_freq_down.read() == 0) {
            g_freq -= 10;
            radio_tune(g_freq);
            memset(g_ps_name, ' ', 8);
        }
        if (g_but_vol_up.read() == 0) {
            if (g_volume < 63) g_volume++;
            radio_set_volume(g_volume);
        }
        if (g_but_vol_down.read() == 0) {
            if (g_volume > 0) g_volume--;
            radio_set_volume(g_volume);
        }

        // --- Data Task: Fetch Status ---
        i2c_start();
        i2c_output(SI4735_ADDRESS | W);
        i2c_output(0x23); // FM_RSQ_STATUS
        i2c_output(0x01);
        i2c_start();
        i2c_output(SI4735_ADDRESS | R);
        i2c_input(); i2c_ack();      // Resp 0: Status
        l_ST_status = i2c_input(); i2c_ack(); // Resp 1: Stereo bit is bit 7
        i2c_input(); i2c_ack();      // Resp 2
        l_RSSI = i2c_input(); i2c_ack();      // Resp 3: RSSI
        // Flush remaining bytes
        for(int i=0; i<3; i++) { i2c_input(); i2c_ack(); }
        i2c_input(); i2c_nack();
        i2c_stop();

        // --- UI Tasks ---
        update_signal_bar(l_RSSI);           // Signal level to Light Bar
        update_rds();                        // Update Station Name
        g_led_stereo.write((l_ST_status & 0x80) ? 0 : 1); // Task: Detect stereo

        PRINTF("\rFreq: %d.%d | Vol: %d | RSSI: %d | Station: [%s]", 
                g_freq/100, g_freq%100, g_volume, l_RSSI, g_ps_name);

        delay_ms(150); // Loop timing/debounce
    }
}