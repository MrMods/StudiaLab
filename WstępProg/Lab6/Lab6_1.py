import matplotlib.pyplot as plt
import numpy as np

#Zad 1
def WykresSlup():
    kategoria = ["owoce", "warzywa", "inne"]
    produkty = [51,123,13]

    plt.bar(kategoria, produkty)            # Tworzenie wyukresu kolumnowego
    plt.title("Ilość sprzedanych produktów w różnych kategoriach")              # Ustawianie tytulu wykresu
    plt.show()              # Wyswietlanie wykresu


WykresSlup()
