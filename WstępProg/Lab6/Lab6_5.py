import numpy as np

#Zad 5

def LosowaMacierz():
    macierz = np.random.randint(low=0, high=50, size=(5,5))                 #Losowanie losowo elementow w miecierzy 5x5, tworzenie macierzy
    print(macierz)
    print(f"Minimalna liczba w macierzy: {macierz.min()}")                  #Minimalna liczba
    print(f"Maksymalna liczba w macierzy: {macierz.max()}")                 #Maksymalna liczba

    print(f"Najwiekszy element w wierszu: {macierz.max(axis=1)}")           #Wyszukanie najwiekszego elementu w wierszu
    print(f"Suma elementów w wierszu: {macierz.sum(axis=1)}")               #Suma elementow w wierszu
    print(f"Najwiekszy element w kolumnie: {macierz.min(axis=0)}")          #Wyszukanie najwiekszego elementu w kolumnie
    print(f"Suma elementów w kolumnie: {macierz.sum(axis=0)}")              #Suma elementow w wierszu

'''
[[46 42 22 41 31]
 [45 41  4 32 26]
 [32  2 20 47 15]
 [42 46  1 48 41]
 [23 26 36  1 24]]
Minimalna liczba w macierzy: 1
Maksymalna liczba w macierzy: 48
Najwiekszy element w wierszu: [46 45 47 48 36]
Suma elementów w wierszu: [182 148 116 178 110]
Najwiekszy element w kolumnie: [23  2  1  1 15]
Suma elementów w kolumnie: [188 157  83 169 137]
'''

LosowaMacierz()