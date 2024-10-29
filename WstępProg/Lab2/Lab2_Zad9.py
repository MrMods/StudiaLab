#Zad 9

def ZamianaWielkosciLiter(x):

    y = x.swapcase()            #Zamiana liter
    print(f"Zmienione wielkości liter: {y}")

'''
Podaj litery do zmiany wielkości: aaDD
Zmienione wielkości liter: AAdd
'''

ZamianaWielkosciLiter(str(input("Podaj litery do zmiany wielkości: ")))            #Wprowadzenie liter