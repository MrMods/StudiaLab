import numpy as np

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


'''
[[0 0 0]
 [0 0 0]
 [0 0 0]]

Macierz a
[[0 0 0]
 [0 0 0]
 [1 1 1]]

Macierz b
[[0 0 0]
 [0 1 0]
 [0 1 0]]

Macierz c
[[0 0 0]
 [1 1 1]
 [1 1 1]]

Macierz d
[[1 0 1]
 [1 0 1]
 [0 0 0]]

Macierz e
[[0 0 0]
 [0 1 1]
 [0 1 1]]
'''

TabZer()