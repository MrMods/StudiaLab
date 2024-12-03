#Zad3

def zmienne():
    imie = str(input("Podaj imie: "))
    print(f"Witaj {imie}")

    wiek = int(input("Podaj wiek: "))
    print(f"Twój wiek to: {wiek}")

    imie = str(input("Podaj imie: "))
    nazwisko = str(input("Podaj nazwisko: "))
    print(f"Inicjaly: {imie[0]}{nazwisko[0]}")              #Pobiera 1 litere z zmiennych

    lancuch = input("Podaj lancuch: ")
    for i in range(0, 5):                                   #Petla wykonuje sie 5 razy
        print(lancuch)

    lancuch1 = input("Podaj lancuch1: ")
    lancuch2 = input("Podaj lancuch2: ")
    lancuch3 = lancuch1 + lancuch2                          #Laczenie 2 lancuchow
    print(lancuch3)

    lancuch1 = input("Podaj lancuch1: ")
    lancuch2 = input("Podaj lancuch2: ")
    lancuch3 = lancuch1[:int(((len(lancuch1)) / 2))] + lancuch2[int(((len(lancuch2)) / 2)):]            #Pobiera 1 polowe z 1 lancuchu i 2 polowe z 2 lancuchu
    print(lancuch3)

'''
Podaj imie: Krystian
Witaj Krystian
Podaj wiek: 23
Twój wiek to: 23
Podaj imie: Krystian
Podaj nazwisko: Zadlo
Inicjaly: KZ
Podaj lancuch: Tata
Tata
Tata
Tata
Tata
Tata
Podaj lancuch1: Mam
Podaj lancuch2: Zadanie
MamZadanie
Podaj lancuch1: Wita
Podaj lancuch2: Moje
Wije
'''

zmienne()