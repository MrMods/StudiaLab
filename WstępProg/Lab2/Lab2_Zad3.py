#Zad 3
def SprawdzanieNazwy():

    Nazwa_pliku = "Raport_maj.xlsx"
    x = Nazwa_pliku.endswith(".xlsx")                   #Sprawdzenie czy nazwa konczy sie na .xlsx

    if x:                                               #Sprawdzenie czy to prawda i wypisanie tak w przeciwnym wypadku nie
        print("Tak")
    else:
        print("Nie")

SprawdzanieNazwy()

#Tak