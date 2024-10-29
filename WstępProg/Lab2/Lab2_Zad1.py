#Zad 1

def RezultatEgzaminu (LiczbaPunktow):
    if LiczbaPunktow > 80:                                                      #Sprawdzenie czy jest zaliczony w 0 terminie
        print("Zaliczony egzamin w terminie 0")
    elif LiczbaPunktow >= 50 and LiczbaPunktow <= 80:                            #Sprawdzenie czy jest z przedziału 50-80
        print("Zaliczony egzamin, można poprawić egzamin")
    else:                                                                       #Sprawdznie czy jest ponizej 50 punktow
        print("Musisz poprawić egzamin")

RezultatEgzaminu(float(input("Podaj liczbe punktow z egzaminu: ")))              #Podanie liczy punktow

'''
Podaj liczbe punktow z egzaminu: 65
Zaliczony egzamin, można poprawić egzamin

Podaj liczbe punktow z egzaminu: 85
Zaliczony egzamin w terminie 0

Podaj liczbe punktow z egzaminu: 42
Musisz poprawić egzamin
'''