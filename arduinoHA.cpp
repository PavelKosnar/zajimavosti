#include <ESP8266WiFi.h>
#include <Ethernet.h>
#include <ArduinoHA.h>

#define BROKER_ADDR IPAddress(192,168,10,22)

byte mac[] = {0x00, 0x10, 0xFA, 0x6E, 0x38, 0x4A};
WiFiClient client;

HADevice device(mac, sizeof(mac));
HAMqtt mqtt(client, device);

// devices types go here
HASwitch switch1("mySwitch1");
HASwitch switch2("mySwitch2");

void onSwitchCommand(bool state, HASwitch* sender)
{
    if (sender == &switch1) {
        // the switch1 has been toggled
        // state == true means ON state
    } else if (sender == &switch2) {
        // the switch2 has been toggled
        // state == true means ON state
    }

    sender->setState(state); // report state back to the Home Assistant
}

void setup() {
     Serial.begin(115200);
  delay(10);
  Serial.println('\n');

  WiFi.mode(WIFI_STA);
  WiFi.begin("ESPNet", "");
  Serial.print("Connecting to ");
  Serial.print("ESPNet"); Serial.println(" ...");

  int i = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }

  Serial.println('\n');
  Serial.println("Connected");  
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());
    // you don't need to verify return status
    

    switch1.setName("Pretty label 1");
    switch1.setIcon("mdi:lightbulb");
    switch1.onCommand(onSwitchCommand);

    switch2.setName("Pretty label 2");
    switch2.setIcon("mdi:lightbulb");
    switch2.onCommand(onSwitchCommand);    

    mqtt.begin(BROKER_ADDR);
}

void loop() {
    Ethernet.maintain();
    mqtt.loop();
}
