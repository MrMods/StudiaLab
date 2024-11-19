#Zad4
def CenaPotraw():
    x = int(input("Podaj liczbe gości: "))
    y = int(input("Podaj liczbe zamowionych potraw: "))
    cena_potraw = 0
    i = 0

    while i<y:
        danie = float(input(f"Podaj cene dania {i+1}: "))
        cena_potraw += danie            #Dodawanie dania do cen potraw
        i+= 1
    if x>0:
        srednia_cena_potrawy = cena_potraw/y                #Obliczanie sredniej ceny potraw
    else:
        print("Liczba potraw musi byc wieksza od zera")

    if x>0:
        sredni_koszt_goscia = cena_potraw/x                 #Obliczanie sredniego kosztu dla goscia
    else:
        print("Liczba gości musi byc wieksza od zera")

    print(f"Koszt zamowienia dla goscia wynosi: {sredni_koszt_goscia:.2f}, Srednia cena potrawy: {srednia_cena_potrawy:.2f}")

CenaPotraw()

'''
Podaj liczbe gości: 2
Podaj liczbe zamowionych potraw: 2
Podaj cene dania 1: 15
Podaj cene dania 2: 60
Koszt zamowienia dla goscia wynosi: 37.50, Srednia cena potrawy: 37.50
'''