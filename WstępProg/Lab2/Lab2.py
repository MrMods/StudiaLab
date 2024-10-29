#Zad 1

def RezultatEgzaminu (LiczbaPunktow):
    if LiczbaPunktow > 80:                                                      #Sprawdzenie czy jest zaliczony w 0 terminie
        print("Zaliczony egzamin w terminie 0")
    elif LiczbaPunktow >= 50 and LiczbaPunktow <= 80:                            #Sprawdzenie czy jest z przedziału 50-80
        print("Zaliczony egzamin, można poprawić egzamin")
    else:                                                                       #Sprawdznie czy jest ponizej 50 punktow
        print("Musisz poprawić egzamin")

#RezultatEgzaminu(float(input("Podaj liczbe punktow z egzaminu: ")))              #Podanie liczy punktow

'''
Podaj liczbe punktow z egzaminu: 65
Zaliczony egzamin, można poprawić egzamin

Podaj liczbe punktow z egzaminu: 85
Zaliczony egzamin w terminie 0

Podaj liczbe punktow z egzaminu: 42
Musisz poprawić egzamin
'''

#Zad 2

def PorzadkowanieLiczb(x,y,z):

    if x > y:                       #Sprawdzenie czy 1 liczba jest wieksza od 2
        x, y = y, x                 #Zamiana wartosci zmiennych x = y, y = x
    if x > z:                       #Sprawdzenie czy 1 liczba jest wieksza od 3
        x, z = z, x                 #Zamiania wartosci zmiennych x = z, z = x
    if y > z:                       #Sprawdzenie czy 2 liczba jest wieksza od 3
        y, z = z, y                 #Zamiania wartosci zmiennych y = z, z = y


    print(f"Liczby od najmniejszej do najwiekszej: {x}, {y}, {z}")

#PorzadkowanieLiczb(float(input("Podaj 1 liczbe: ")),float(input("Podaj 2 liczbe: ")),float(input("Podaj 3 liczbe: ")))                  #Podanie liczb

'''
Podaj 1 liczbe: 31.4
Podaj 2 liczbe: 9
Podaj 3 liczbe: 13.8
Liczby od najmniejszej do najwiekszej: 9.0, 13.8, 31.4
'''

#Zad 3
def SprawdzanieNazwy():

    Nazwa_pliku = "Raport_maj.xlsx"
    x = Nazwa_pliku.endswith(".xlsx")                   #Sprawdzenie czy nazwa konczy sie na .xlsx

    if x:                                               #Sprawdzenie czy to prawda i wypisanie tak w przeciwnym wypadku nie
        print("Tak")
    else:
        print("Nie")

#Tak

#SprawdzanieNazwy()

#Zad 4
def DruzynaPilkarska(gol):
    bonus = int(0)                                      #Zmienna bonus
    bonusb = int(0)                                     #Zmienna bonus do podpunktu b)

    if gol > 0:                                         #Jezeli jest jakas bramka
        bonus += gol * 10                               #Dodanie bonusu za kazda bramke
        bonusb = bonus                                      #Dodanie do zmiennej bonusb punktow za bramki

    if gol > 5 and gol <= 10:                           #Sprawdzenie czy jest wiecej niz 5 bramek i nie wiecej niz 10
        bonus += 5                                      #Dodanie do zmiennej bonus 5 punktow
        bonusb = bonus                                      #Dodanie do zmiennej bonusb punktow gdy nie ma wiecej niz 10 bramek

    elif gol > 10:                                      #Sprawdznie czy jest wiecej niz 10 goli
        bonus += 10                                     #Dodanie do zmiennej bonus 10 punktow
        bonusb = bonus + 5                                  #Suma obydwu bonusow (5, 10 punktow)

    print(f"a) Punkty zdobyte z bramek, punkty bonusowe: {bonus} punktow")
    print(f"b) Punkty zdobyte z bramek, punkty bonusowe: {bonusb} punktow")


'''
Podaj liczbe strzelonych bramek: 15
a) Punkty zdobyte z bramek, punkty bonusowe: 160 punktow
b) Punkty zdobyte z bramek, punkty bonusowe: 165 punktow
'''

#DruzynaPilkarska(int(input("Podaj liczbe strzelonych bramek: ")))

#Zad 5
def OperacjeNaPliku():

    with open("notowania_gieldowe.txt", "r") as plik:               #Zczytywanie z pliku i wypisywanie po lini
        for line in plik:
            print(line, end="")

    with open("notowania_gieldowe.txt", "a") as plik:               #Dodawanie w nowej lini wartosci
        plik.writelines("ADR, 113 \n")

    with open("notowania_gieldowe.txt", "r") as plik:               #Zczytywanie z pliku i wypisywanie po lini
        for line in plik:
            print(line, end="")

#OperacjeNaPliku()

#Zad 6

def SprawdzanieDuzejLitery(litera):

   if litera.isalpha() and len(litera) == 1:                #Sprawdzenie czy jest jedna litera
       if litera.isupper():                                 #Sprawdzenie czy jest duza litera
           print(f"Litera: {litera} jest dużą literą.")
       else:
           print(f"Litera: {litera} jest małą literą.")     #Sprawdzenie czy jest mala
   else:
       print("Wprowadzony znak nie jest pojedynczą literą.")

#SprawdzanieDuzejLitery(input("Podaj litere: "))

'''
Podaj litere: D
Litera: D jest dużą literą.

'''

#Zad 7
def haslo():

    haslo = 'pk47!jy0893'

    if len(haslo) >= 11 and "!" in haslo:           #Sprawdzenie czy haslo jest dluzsze od 11 znakow oraz czy zawiera !
        print("Hasło jest poprawne")
    else:
        print("Hasło jest nie poprawne")

#Hasło jest poprawne

#haslo()

#Zad 8
def wycinanie():

    text = 'Studiuje-Informatykę'

    x = text[0:3]           #Wyciecie 3 pierwszych znakow
    y = text[-2:]           #Wyciecie 2 ostatnich znakow

    print(f"Pierwsze 3 znaki: '{x}', Ostatnie 2 znaki: '{y}'")

#Pierwsze 3 znaki: 'Stu', Ostatnie 2 znaki: 'kę'

#wycinanie()

#Zad 9

def ZamianaWielkosciLiter(x):

    y = x.swapcase()            #Zamiana liter
    print(f"Zmienione wielkości liter: {y}")

'''
Podaj litery do zmiany wielkości: aaDD
Zmienione wielkości liter: AAdd
'''
#ZamianaWielkosciLiter(str(input("Podaj litery do zmiany wielkości: ")))            #Wprowadzenie liter