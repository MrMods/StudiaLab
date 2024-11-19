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

Paliwo()

'''
Ilość paliwa: 100
Czas lotu: 1
Ilość paliwa: 90
Czas lotu: 2
Ilość paliwa: 80
Czas lotu: 3
Ilość paliwa: 70
Czas lotu: 4
Ilość paliwa: 60
Czas lotu: 5
Ilość paliwa: 50
Czas lotu: 6
Ilość paliwa: 40
Czas lotu: 7
Ilość paliwa: 30
Czas lotu: 8
Ilość paliwa: 20
Czas lotu: 9
Ilość paliwa: 10
Czas lotu: 10
Koniec lotu...
'''