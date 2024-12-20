import random
import math

def SredniaGeometryczna():
    liczby = []

    zakres1 = int(input("Podaj najmniejszą liczbe zakresu:"))                               #podawanie zakresu
    zakres2 = int(input("Podaj najwieksza liczbe zakresu:"))
    if zakres1 > zakres2:                                                                   #Sprawdzenie czy zakres jest poprawny
        print("Zakres nie może zaczynać sie od większej liczby")
        return

    for i in range (0, 10):                                                                 #Losoawnie 10 liczb z zakresu
        liczby.append(random.randint(zakres1, zakres2))

    print(f"Wylosowana krotka: {liczby}")

    iloczyn = math.prod(liczby)                                                             #Iloczyn n liczb
    n = len(liczby)                                                                         #ilosc elementow krotki

    sr_geo = iloczyn ** (1/n)                                                               #Obliczanie sredniej geometrycznej
    print(f"Srednia geometryczna: {sr_geo}")

SredniaGeometryczna()


'''
Podaj najmniejszą liczbe zakresu:5
Podaj najwieksza liczbe zakresu:15
Wylosowana krotka: [12, 11, 15, 6, 5, 5, 7, 10, 15, 8]
Srednia geometryczna: 8.703693190696042

'''