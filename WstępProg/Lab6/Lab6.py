

import matplotlib.pyplot as plt
import numpy as np

#Zad 1
def WykresSlup():
    kategoria = ["owoce", "warzywa", "inne"]
    produkty = [51,123,13]

    plt.bar(kategoria, produkty)            #Tworzenie wyukresu kolumnowego
    plt.title("Ilość sprzedanych produktów w różnych kategoriach")          #Ustawianie tytulu wykresu
    plt.show()                                                          #Wyswietlanie wykresu

#WykresSlup()

#Zad 2
def WykresKol():
    kategoria = ["owoce", "warzywa", "inne"]
    produkty = [51, 100, 13]

    plt.pie(produkty, labels=kategoria, autopct="%1.f%%")           #Tworzenie wykresu kolowego, pokazywanie wartosci,
    plt.title("Procentowy udział różnych kategorii sprzedaży")       #Ustawianie tytulu wykresu
    plt.show()                                                      #Wyswietlanie wykresu

#WykresKol()

#Zad 3

def WykresPunkt():
    x = [1, 2, 3, 4, 5]
    y = [25, 12, 87, 44, 10]

    plt.scatter(x,y)                #Tworzenie wykresu punktowego
    plt.xlabel("Czas")              #Ustawianie tytulu osi x
    plt.ylabel("Prędkość chwilowa pojazdu")     #Ustawianie tytulu osi y

    plt.show()                      #Wyswietlanie wykresu


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
    macierz = np.random.randint(low=0, high=50, size=(5,5))                 #Losowanie losowo elementow w miecierzy 5x5, tworzenie macierzy
    print(macierz)
    print(f"Minimalna liczba w macierzy: {macierz.min()}")                  #Minimalna liczba
    print(f"Maksymalna liczba w macierzy: {macierz.max()}")                 #Maksymalna liczba

    print(f"Najwiekszy element w wierszu: {macierz.max(axis=1)}")           #Wyszukanie najwiekszego elementu w wierszu
    print(f"Suma elementów w wierszu: {macierz.sum(axis=1)}")               #Suma elementow w wierszu
    print(f"Najwiekszy element w kolumnie: {macierz.min(axis=0)}")          #Wyszukanie najwiekszego elementu w kolumnie
    print(f"Suma elementów w kolumnie: {macierz.sum(axis=0)}")              #Suma elementow w wierszu

#LosowaMacierz()


#Zad 6

def TabZer():
    macierz = np.zeros((3,3), dtype=int)            #Macierz wypelniowna zerami
    print(f"{macierz}\n")

    print("Macierz a")
    macierz_a = macierz.copy()          #Kopia macierzy
    macierz_a[2, :] = 1                 #Zamiania dolnego wiersza 1
    print(f"{macierz_a}\n")

    print("Macierz b")
    macierz_b = macierz.copy()          #Kopia macierzy
    macierz_b[1:, 1] = 1                 #Zamiania srodkowej kolumny bez górnego wiersza 1
    print(f"{macierz_b}\n")

    print("Macierz c")
    macierz_c = macierz.copy()          #Kopia macierzy
    macierz_c[1:, :] = 1                 #Zamiania srodkowego i dolnego wiersza 1
    print(f"{macierz_c}\n")

    print("Macierz d")
    macierz_d = macierz.copy()          #Kopia macierzy
    macierz_d[:2, 0] = 1                 #Zamiania pierwszej kolumny bez dolu 1
    macierz_d[:2, 2] = 1                 #Zamiania ostatnie kolumny bez dolu 1
    print(f"{macierz_d}\n")

    print("Macierz e")
    macierz_e = macierz.copy()          #Kopia macierzy
    macierz_e[1:, 1] = 1                 #Zamiania srodkowej kolumny bez gory 1
    macierz_e[1:, 2] = 1                 #Zamiania ostatniej kolumny bez gory 1
    print(f"{macierz_e}\n")

#TabZer()

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

#Zamiana()

#Zad 8

def Macierz5Losowe():
    macierz = np.random.randint(low=0, high=50, size=(5,5))              #Losowanie losowo elementow w miecierzy 5x5, tworzenie macierzy
    print(f"Macierz \n {macierz}")
    elementy_wieksze_od_20 = macierz[macierz > 20]                       #Zapisywanie elementow wiekszych od 20 w macierzy
    liczba_elementow = elementy_wieksze_od_20.size                       #Sprawdzanie Wielksci tablicy (liczba elementow)
    print(f"Liczba elementow wiekszych od 20: {liczba_elementow}")
    print(f"Srednia elementow wiekszych od 20: {elementy_wieksze_od_20.mean()}")           #Srednia elementow wiekszych od 20
    print(f"Srednia macierzy: {macierz.mean()}")                         #Srednia calej macierzy

#Macierz5Losowe()