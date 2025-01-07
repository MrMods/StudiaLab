import matplotlib.pyplot as plt
import numpy as np

#Zad 2
def WykresKol():
    kategoria = ["owoce", "warzywa", "inne"]
    produkty = [51, 100, 13]

    plt.pie(produkty, labels=kategoria, autopct="%1.f%%")           #Tworzenie wykresu kolowego, pokazywanie wartosci,
    plt.title("Procentowy udział różnych kategorii sprzedaży")       #Ustawianie tytulu wykresu
    plt.show()                                                      #Wyswietlanie wykresu

WykresKol()