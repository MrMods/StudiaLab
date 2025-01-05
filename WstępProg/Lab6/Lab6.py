from random import randint, randrange

import matplotlib.pyplot as plt
import numpy as np

#Zad 1
def WykresSlup():
    kategoria = ["owoce", "warzywa", "inne"]
    produkty = [51,123,13]

    plt.bar(kategoria, produkty)
    plt.title("Ilość sprzedanych produktów w różnych kategoriach")
    plt.show()

#WykresSlup()

#Zad 2
def WykresKol():
    kategoria = ["owoce", "warzywa", "inne"]
    produkty = [51, 100, 13]

    plt.pie(produkty, labels=kategoria, autopct="%1.f%%")
    plt.title("Procentowy udział różnych kategorii sprzedaży")
    plt.show()

#WykresKol()

#Zad 3

def WykresPunkt():
    x = [1, 2, 3, 4, 5]
    y = [25, 12, 87, 44, 10]

    plt.scatter(x,y)
    plt.xlabel("Czas")
    plt.ylabel("Prędkość chwilowa pojazdu")

    plt.show()


#WykresPunkt()

#Zad 4
def ndLista():
    Liczby2 = [128,64,32,16,8,4,2,1]
    LiczbyBin = [1,1,0,0,1,0,1,1]

    wagi = np.array(Liczby2)
    liczba_bin = np.array(LiczbyBin)

    def wartosc_liczby_bin():
        LiczbaDziesietna = 0
        for i in range(0,8):                    #Sprawdzanie kazdej liczby w tablicy
            spr_bin = liczba_bin[i] == 1        #Sprawdzanie czy liczba w tablicy jest 1
            if spr_bin:
                LiczbaDziesietna += Liczby2[i]      #Dodanie liczby z wagi do liczby dziesietnej
        return LiczbaDziesietna

    print(f"Wartość liczby binarnej zamienionej na dziesiętną = {wartosc_liczby_bin()}")

#ndLista()

#Zad 5

def LosowaMacierz():
    macierz = np.random.randint(low=0, high=50, size=(5,5))
    print(macierz)
    print(f"Minimalna liczba w macierzy: {macierz.min()}")
    print(f"Maksymalna liczba w macierzy: {macierz.max()}")

    index = macierz.argmin(axis = 1)
    print(macierz[index,0])

LosowaMacierz()