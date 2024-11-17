#Zad1
def Paliwo():
    paliwo = 100
    paliwo_zuzyte_na_s = 10
    czas = 0

    while paliwo>0:
        print(f"Ilość paliwa: {paliwo}")
        czas += 1
        paliwo = paliwo - paliwo_zuzyte_na_s
        print(f"Czas lotu: {czas}")
    else:
        print("Koniec lotu...")

##Paliwo()

#Zad2
def LiczbaPierwsza():
    liczba_pierwsze = []
    liczba = 2
    licznik = 0
    while len(liczba_pierwsze) < 10:
        for licznik in range (2, liczba):
            if liczba % 2 == 0:
                break
        else:
            liczba_pierwsze.append(liczba)
        liczba += 1
    print(liczba_pierwsze)

##LiczbaPierwsza()

#Zad3
def Ulice():
    ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

    for u in ulice:
        for b in range(5):
            for l in range(10):
                print(f"Ulica: {u}, Blok:{b+1}, Lokal: {l+1}")

##Ulice()

#Zad4
def CenaPotraw():
    x = int(input("Podaj liczbe gości: "))
    y = int(input("Podaj liczbe zamowionych potraw: "))
    cena_potraw = 0
    i = 0

    while i<y:
        danie = float(input(f"Podaj cene dania {i+1}: "))
        cena_potraw += danie
        i+= 1
    if x>0:
        srednia_cena_potrawy = cena_potraw/y
    else:
        print("Liczba potraw musi byc wieksza od zera")

    if x>0:
        sredni_koszt_goscia = cena_potraw/x
    else:
        print("Liczba gości musi byc wieksza od zera")

    print(f"Koszt zamowienia dla goscia wynosi: {sredni_koszt_goscia:.2f}, Srednia cena potrawy: {srednia_cena_potrawy:.2f}")

##CenaPotraw()


#Zad5
def ListaLiczb():
    listaliczb = []
    for i in range(80, -1 , -4):
        listaliczb.append(i)

    print(listaliczb)

##ListaLiczb()

#Zad6
def Pentla():
    liczba = 0
    while liczba> 0:

    print("dsd")

#Pentla()
