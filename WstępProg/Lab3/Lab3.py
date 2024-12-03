#Zad1
def Paliwo():
    paliwo = 100
    paliwo_zuzyte_na_s = 10
    czas = 0

    while paliwo>0:             #Jeżeli paliwo jest większe od 0 to pętla się wykona
        print(f"Ilość paliwa: {paliwo}")
        czas += 1               #Dodawanie czasu
        paliwo = paliwo - paliwo_zuzyte_na_s        #Obliczanie zużycia paliwa
        print(f"Czas lotu: {czas}")
    else:
        print("Koniec lotu...")

##Paliwo()

#Zad2
def LiczbaPierwsza():
    liczba_pierwsze = []        #Lista z liczbami pierwszymi
    liczba = 2
    licznik = 0
    while len(liczba_pierwsze) < 10:        #Jeszeli liczba liczb pierwszych jest mniejsza od 10, petla sie wykonuje
        for licznik in range (2, liczba):       #Petla dla kazdej liczby od 2 do liczby
            if liczba % licznik == 0:                 #Sprawdzanie parzystosci, jezeli true to nie moze byc pierwsza
                break
        else:
            liczba_pierwsze.append(liczba)      #Dodawanie do listy liczby pierwszej
        liczba += 1
    print(liczba_pierwsze)

#LiczbaPierwsza()

#Zad3
def Ulice():
    ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]   #Lista ulic

    for u in ulice:                 #Petla dla ulic
        for b in range(5):          #Petla dla blokow
            for l in range(10):     #Petla dla lokali
                print(f"Ulica: {u}, Blok:{b+1}, Lokal: {l+1}")          #Wypisywanie danej ulicy, bloku, lokalu w kazdym przypadku wykanania petli

##Ulice()

#Zad4
def CenaPotraw():
    x = int(input("Podaj liczbe gości: "))
    y = int(input("Podaj liczbe zamowionych potraw: "))
    cena_potraw = 0
    i = 0

    while i<y:
        danie = float(input(f"Podaj cene dania {i+1}: "))
        cena_potraw += danie            #Dodawanie dania do cen potraw
        i+= 1
    if x>0:
        srednia_cena_potrawy = cena_potraw/y                #Obliczanie sredniej ceny potraw
    else:
        print("Liczba potraw musi byc wieksza od zera")

    if x>0:
        sredni_koszt_goscia = cena_potraw/x                 #Obliczanie sredniego kosztu dla goscia
    else:
        print("Liczba gości musi byc wieksza od zera")

    print(f"Koszt zamowienia dla goscia wynosi: {sredni_koszt_goscia:.2f}, Srednia cena potrawy: {srednia_cena_potrawy:.2f}")

##CenaPotraw()


#Zad5
def ListaLiczb():
    listaliczb = []                     #Lista liczb
    for i in range(80, -1 , -4):        #Petla od 80 do 0 co 4 kroki
        listaliczb.append(i)            #Dodawanie do listy liczb

    print(listaliczb)

##ListaLiczb()

#Zad6
def Pentla():
    while True:                                         #Petla nieskonczona
        liczba = int(input("Podaj liczbe: "))           #Podawanie liczby
        if liczba < 0:                                  #Sprawdzanie czy liczba jest ujemna
            print("Liczba ujemna wychodze z pętli")
            break                                       #Wychodzenie z petli
##Pentla()

#Zad 7
def GrupaLaboratoryjnaA():
    Punkty = []
    i = 0
    Dodawanie_Punktow = 0
    Srednia_Punktow = 0

    Studenci = int(input("Podaj liczbe studentów: "))
    for Studenci in range (0, Studenci):                                            #Petla dla kazdego studenta aby podac liczbe punktow
        p = float(input(f"Podaj liczbe punktow dla studenta {Studenci + 1}: "))
        if not p > 0 or not p < 100:                                                #Sprawdzanie zakresu punktow od 0 do 100
            continue
        Punkty.append(p)                    #Dodawanie do listy punktow

    else:
        if len(Punkty) > 0:                             #jezeli liczba punktow jest powyzej 0
            while i < len(Punkty):                      #Petla dodajaca punkty do siebie
                Dodawanie_Punktow += Punkty[i]          #Dodawanie punktow z listy
                i+=1
            else:
                Srednia_Punktow = Dodawanie_Punktow / len(Punkty)           #Obliczanie sredniej punktow
                print(f"Srednia liczba punktow grupy: {Srednia_Punktow}")

##GrupaLaboratoryjnaA()

def GrupaLaboratoryjnaB():
    Punkty = []
    i = 0
    Dodawanie_Punktow = 0
    Srednia_Punktow = 0

    Studenci = int(input("Podaj liczbe studentów: "))
    for Studenci in range(0, Studenci):  # Petla dla kazdego studenta aby podac liczbe punktow
        p = float(input(f"Podaj liczbe punktow dla studenta {Studenci + 1}: "))
        if not p > 0 or not p < 100:  # Sprawdzanie zakresu punktow od 0 do 100
            continue
        Punkty.append(p)  # Dodawanie do listy punktow

    else:
        if len(Punkty) > 0:                     # jezeli liczba punktow jest powyzej 0
            while True:                         # Petla nieskonczona
                if i > len(Punkty) - 1:         # Jezeli i jest wieksze od liczby studentow oblicza srednia i przerywa petle
                    Srednia_Punktow = Dodawanie_Punktow / len(Punkty)  # Obliczanie sredniej punktow
                    print(f"Srednia liczba punktow grupy: {Srednia_Punktow}")
                    break
                Dodawanie_Punktow += Punkty[i]  # Dodawanie punktow z listy
                i += 1

##GrupaLaboratoryjnaB()

#Zad 8
def Lancuch():
    tekst ="Python jest super"

    print(tekst[0])
    print(tekst[-1])
    print(tekst[0:-1:2])
    print(tekst[1:-1:3])
    print(tekst[10:-1])
    print(tekst[::-1])

##Lancuch()

#Zad 9
def Ostatnie():

    imie = str(input("Podaj imie: "))
    print(f"Witaj {imie}")

    wiek = int(input("Podaj wiek: "))
    print("Twoj wiek to:", wiek)

    imie = str(input("Podaj imie: "))
    nazwisko = str(input("Podaj nazwisko: "))
    print(f"Inicjaly: {imie[0]}{nazwisko[0]}")

    lancuch = input("Podaj lancych: ")
    for i in range (0, 5):
        print(lancuch)


    lancuch1 = input("Podaj lancych1: ")
    lancuch2 = input("Podaj lancych2: ")
    lancuch3 = lancuch1 + lancuch2
    print(lancuch3)


    lancuch1 = input("Podaj lancych1: ")
    lancuch2 = input("Podaj lancych2: ")
    x = lancuch1 + lancuch2
    y = lancuch1 + lancuch2

    lancuch3 = x[0:int(len(y)/2)]
    print(lancuch3)

##Ostatnie()
