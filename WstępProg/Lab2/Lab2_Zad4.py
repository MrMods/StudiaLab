#Zad 4
def DruzynaPilkarska(gol):
    bonus = int(0)                                      #Zmienna bonus
    bonusb = int(0)                                     #Zmienna bonus do podpunktu b)

    if gol > 0:                                         #Jezeli jest jakas bramka
        bonus += gol * 10                               #Dodanie bonusu za kazda bramke
        bonusb = bonus                                      #Dodanie do zmiennej bonusb punktow za bramki

    if gol > 5 and gol <= 10:                           #Sprawdzenie czy jest wiecej niz 5 bramek i nie wiecej niz 10
        bonus += 5                                      #Dodanie do zmiennej bonus 5 punktow
        bonusb = bonus                                      #Dodanie do zmiennej bonusb punktow gdy nie ma wiecej niz 10 bramek

    elif gol > 10:                                      #Sprawdznie czy jest wiecej niz 10 goli
        bonus += 10                                     #Dodanie do zmiennej bonus 10 punktow
        bonusb = bonus + 5                                  #Suma obydwu bonusow (5, 10 punktow)

    print(f"a) Punkty zdobyte z bramek, punkty bonusowe: {bonus} punktow")
    print(f"b) Punkty zdobyte z bramek, punkty bonusowe: {bonusb} punktow")


'''
Podaj liczbe strzelonych bramek: 15
a) Punkty zdobyte z bramek, punkty bonusowe: 160 punktow
b) Punkty zdobyte z bramek, punkty bonusowe: 165 punktow
'''

DruzynaPilkarska(int(input("Podaj liczbe strzelonych bramek: ")))
