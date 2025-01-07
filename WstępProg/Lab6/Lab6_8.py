import numpy as np

#Zad 8

def Macierz5Losowe():
    macierz = np.random.randint(low=0, high=50, size=(5,5))              #Losowanie losowo elementow w miecierzy 5x5, tworzenie macierzy
    print(f"Macierz \n {macierz}")
    elementy_wieksze_od_20 = macierz[macierz > 20]                       #Zapisywanie elementow wiekszych od 20 w macierzy
    liczba_elementow = elementy_wieksze_od_20.size                       #Sprawdzanie Wielksci tablicy (liczba elementow)
    print(f"Liczba elementow wiekszych od 20: {liczba_elementow}")
    print(f"Srednia elementow wiekszych od 20: {elementy_wieksze_od_20.mean()}")           #Srednia elementow wiekszych od 20
    print(f"Srednia macierzy: {macierz.mean()}")                         #Srednia calej macierzy

'''
Macierz 
 [[ 5 29  8 21  6]
 [38 39  0 19 15]
 [29 24 39 42 48]
 [48 23 34 49  6]
 [27 32 49 23  8]]
Liczba elementow wiekszych od 20: 17
Srednia elementow wiekszych od 20: 34.94117647058823
Srednia macierzy: 26.44
'''



Macierz5Losowe()