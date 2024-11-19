# Zad 9
def Ostatnie():
    imie = str(input("Podaj imie: "))
    print(f"Witaj {imie}")

    wiek = int(input("Podaj wiek: "))
    print("Twoj wiek to:", wiek)

    imie = str(input("Podaj imie: "))
    nazwisko = str(input("Podaj nazwisko: "))
    print(f"Inicjaly: {imie[0]}{nazwisko[0]}")

    lancuch = input("Podaj lancuch: ")
    for i in range(0, 5):
        print(lancuch)

    lancuch1 = input("Podaj lancuch1: ")
    lancuch2 = input("Podaj lancuch2: ")
    lancuch3 = lancuch1 + lancuch2
    print(lancuch3)

    lancuch1 = input("Podaj lancuch1: ")
    lancuch2 = input("Podaj lancuch2: ")
    x = lancuch1 + lancuch2
    y = lancuch1 + lancuch2

    lancuch3 = x[0:int(len(y) / 2)]
    print(lancuch3)


Ostatnie()

'''
Podaj imie: Krystian
Podaj nazwisko: Zadlo
Inicjaly: KZ
Podaj lancuch: Witaj
Witaj
Witaj
Witaj
Witaj
Witaj
Podaj lancuch1: Wataj
Podaj lancuch2: Potaj
WatajPotaj
Podaj lancuch1: Dobry
Podaj lancuch2: Dzien
Dobry
'''