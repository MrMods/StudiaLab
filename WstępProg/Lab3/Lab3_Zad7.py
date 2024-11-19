#Zad 7
def GrupaLaboratoryjnaA():
    Punkty = []
    i = 0
    Dodawanie_Punktow = 0
    Srednia_Punktow = 0

    Studenci = int(input("Podaj liczbe studentów: "))
    for Studenci in range (0, Studenci):                                            #Petla dla kazdego studenta aby podac liczbe punktow
        p = float(input(f"Podaj liczbe punktow dla studenta {Studenci + 1}: "))
        if not p > 0 or not p < 100:                                                #Sprawdzanie zakresu punktow od 0 do 100
            continue
        Punkty.append(p)                    #Dodawanie do listy punktow

    else:
        if len(Punkty) > 0:                             #jezeli liczba punktow jest powyzej 0
            while i < len(Punkty):                      #Petla dodajaca punkty do siebie
                Dodawanie_Punktow += Punkty[i]          #Dodawanie punktow z listy
                i+=1
            else:
                Srednia_Punktow = Dodawanie_Punktow / len(Punkty)           #Obliczanie sredniej punktow
                print(f"Srednia liczba punktow grupy: {Srednia_Punktow}")

GrupaLaboratoryjnaA()

'''
Podaj liczbe studentów: 2
Podaj liczbe punktow dla studenta 1: 50
Podaj liczbe punktow dla studenta 2: 60
Srednia liczba punktow grupy: 55.0
'''

def GrupaLaboratoryjnaB():
    Punkty = []
    i = 0
    Dodawanie_Punktow = 0
    Srednia_Punktow = 0

    Studenci = int(input("Podaj liczbe studentów: "))
    for Studenci in range(0, Studenci):  # Petla dla kazdego studenta aby podac liczbe punktow
        p = float(input(f"Podaj liczbe punktow dla studenta {Studenci + 1}: "))
        if not p > 0 or not p < 100:  # Sprawdzanie zakresu punktow od 0 do 100
            continue
        Punkty.append(p)  # Dodawanie do listy punktow

    else:
        if len(Punkty) > 0:                     # jezeli liczba punktow jest powyzej 0
            while True:                         # Petla nieskonczona
                if i > len(Punkty) - 1:         # Jezeli i jest wieksze od liczby studentow oblicza srednia i przerywa petle
                    Srednia_Punktow = Dodawanie_Punktow / len(Punkty)  # Obliczanie sredniej punktow
                    print(f"Srednia liczba punktow grupy: {Srednia_Punktow}")
                    break
                Dodawanie_Punktow += Punkty[i]  # Dodawanie punktow z listy
                i += 1

GrupaLaboratoryjnaB()

'''
Podaj liczbe studentów: 2
Podaj liczbe punktow dla studenta 1: 56
Podaj liczbe punktow dla studenta 2: 15
Srednia liczba punktow grupy: 35.5
'''