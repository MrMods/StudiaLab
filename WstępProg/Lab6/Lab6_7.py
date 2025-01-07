import numpy as np

#Zad 7

def  Zamiana():
    macierz = np.zeros((5,5), dtype=int)

    macierz[0,:] = 1            #Gorna linia
    macierz[-1,:] = 1           #Dolna linia
    macierz[:,0] = 1            #Lewa linia
    macierz[:,-1] = 1           #Prawa linia

    def ZamianaWartosci():
        return np.where(macierz == 0, 1, 0)         #Zamiana 0 1 za pomoca funkcji where

    print(f"Macierz:\n {macierz}")
    print(f"Macierz po zamianie:\n {ZamianaWartosci()}")


'''
Macierz:
 [[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 0 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]
Macierz po zamianie:
 [[0 0 0 0 0]
 [0 1 1 1 0]
 [0 1 1 1 0]
 [0 1 1 1 0]
 [0 0 0 0 0]]
'''

Zamiana()