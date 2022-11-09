rom_to_num = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def kontrola_zadani(text):
    zadani = input(text)
    return zadani.upper()


def vypocet():
    spravne_zadani = kontrola_zadani('Zadejte rimske cislo: ')
    for i in spravne_zadani:
        if i not in rom_to_num:
            spravne_zadani = kontrola_zadani('Spatne zadani, zkuste to znovu: ')

    delka = len(spravne_zadani)
    vysledek = 0
    i = 0

    while i < delka:
        if rom_to_num[spravne_zadani[0]] >= rom_to_num[spravne_zadani[1]]:
            vysledek += rom_to_num[spravne_zadani[0]]
            spravne_zadani = spravne_zadani[1:]
            i += 1
        else:
            vysledek += rom_to_num[spravne_zadani[1]] - rom_to_num[spravne_zadani[0]]
            spravne_zadani = spravne_zadani[2:]
            i += 2
    print(vysledek)


if __name__ == '__main__':
    vypocet()
