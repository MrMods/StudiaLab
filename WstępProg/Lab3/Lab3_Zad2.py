#Zad2
def LiczbaPierwsza():
    liczba_pierwsze = []        #Lista z liczbami pierwszymi
    liczba = 2
    licznik = 0
    while len(liczba_pierwsze) < 10:        #Jeszeli liczba liczb pierwszych jest mniejsza od 10, petla sie wykonuje
        for licznik in range (2, liczba):       #Petla dla kazdej liczby od 2 do liczby
            if liczba % licznik == 0:                 #Sprawdzanie parzystosci
                break
        else:
            liczba_pierwsze.append(liczba)      #Dodawanie do listy liczby pierwszej
        liczba += 1
    print(liczba_pierwsze)

LiczbaPierwsza()

'''[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]'''