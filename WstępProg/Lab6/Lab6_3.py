import matplotlib.pyplot as plt
import numpy as np


#Zad 3

def WykresPunkt():
    x = [1, 2, 3, 4, 5]
    y = [25, 12, 87, 44, 10]

    plt.scatter(x,y)                #Tworzenie wykresu punktowego
    plt.xlabel("Czas")              #Ustawianie tytulu osi x
    plt.ylabel("Prędkość chwilowa pojazdu")     #Ustawianie tytulu osi y

    plt.show()                      #Wyswietlanie wykresu


WykresPunkt()