#Zad 1

def RezultatEgzaminu (LiczbaPunktow):
    if LiczbaPunktow > 80:                                                      #Sprawdzenie czy jest zaliczony w 0 terminie
        print("Zaliczony egzamin w terminie 0")
    elif LiczbaPunktow >= 50 and LiczbaPunktow <= 80:                            #Sprawdzenie czy jest z przedziału 50-80
        print("Zaliczony egzamin, można poprawić egzamin")
    else:                                                                       #Sprawdznie czy jest ponizej 50 punktow
        print("Musisz poprawić egzamin")

#RezultatEgzaminu(float(input("Podaj liczbe punktow z egzaminu: ")))              #Podanie liczy punktow

#Zad 2

def PorzadkowanieLiczb(x,z,y):
    najwieksza = 0
    srodek = 0
    najmniejsza = 0


    print(f"Liczby od najmniejszej do najwiekszej: {najmniejsza}, {srodek}, {najwieksza}")

PorzadkowanieLiczb(6,2,4)

#Zad 3

Nazwa_pliku = "Raport_maj.xlsx"
x = Nazwa_pliku.endswith(".xlsx")                   #Srawdzenie czy nazwa konczy sie na .xlsx

if x:                                               #Sprawdzenie czy to prawda i wypisanie tak w przeciwnym wypadku nie
    print("Tak")
else:
    print("Nie")


#Zad 4



#Zad 5
'''
with open("notowania_gieldowe.txt", "r") as plik:               #Zczytywanie z pliku i wypisywanie po lini
    for line in plik:                   
        print(line, end="")

with open("notowania_gieldowe.txt", "a") as plik:               #Dodawanie w nowej lini wartosci
    plik.writelines("ADR, 113 \n")

with open("notowania_gieldowe.txt", "r") as plik:               #Zczytywanie z pliku i wypisywanie po lini
    for line in plik:
        print(line, end="")
'''

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

#Zad 7

haslo = 'pk47!jy0893'

if len(haslo) >= 11 and "!" in haslo:
    print("Hasło jest poprawne")
else:
    print("Hasło jest nie poprawne")

#Zad 8

