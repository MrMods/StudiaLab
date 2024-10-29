#Zad 2

def PorzadkowanieLiczb(x,y,z):

    if x > y:                       #Sprawdzenie czy 1 liczba jest wieksza od 2
        x, y = y, x                 #Zamiana wartosci zmiennych x = y, y = x
    if x > z:                       #Sprawdzenie czy 1 liczba jest wieksza od 3
        x, z = z, x                 #Zamiania wartosci zmiennych x = z, z = x
    if y > z:                       #Sprawdzenie czy 2 liczba jest wieksza od 3
        y, z = z, y                 #Zamiania wartosci zmiennych y = z, z = y


    print(f"Liczby od najmniejszej do najwiekszej: {x}, {y}, {z}")

PorzadkowanieLiczb(float(input("Podaj 1 liczbe: ")),float(input("Podaj 2 liczbe: ")),float(input("Podaj 3 liczbe: ")))                  #Podanie liczb

'''
Podaj 1 liczbe: 31.4
Podaj 2 liczbe: 9
Podaj 3 liczbe: 13.8
Liczby od najmniejszej do najwiekszej: 9.0, 13.8, 31.4
'''