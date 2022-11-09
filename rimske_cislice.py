rom_to_num = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def dostat_zadani(text):
    rimske_cislice = input(text)
    return rimske_cislice.upper()


def vypocet():
    zadani = dostat_zadani('Zadejte rimske cislo: ')
    for i in zadani:
        if i not in rom_to_num:
            zadani = dostat_zadani('Spatne zadani, zkuste to znovu: ')

    delka = len(zadani)
    vysledek = 0
    i = 0

    while i < delka:
        if rom_to_num[zadani[0]] >= rom_to_num[zadani[1]]:
            vysledek += rom_to_num[zadani[0]]
            zadani = zadani[1:]
            i += 1
        else:
            vysledek += rom_to_num[zadani[1]] - rom_to_num[zadani[0]]
            zadani = zadani[2:]
            i += 2
    print(vysledek)


if __name__ == '__main__':
    vypocet()
