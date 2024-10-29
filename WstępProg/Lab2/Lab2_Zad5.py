#Zad 5
def OperacjeNaPliku():

    with open("notowania_gieldowe.txt", "r") as plik:               #Zczytywanie z pliku i wypisywanie po lini
        for line in plik:
            print(line, end="")

    with open("notowania_gieldowe.txt", "a") as plik:               #Dodawanie w nowej lini wartosci
        plik.writelines("ADR, 113 \n")

    with open("notowania_gieldowe.txt", "r") as plik:               #Zczytywanie z pliku i wypisywanie po lini
        for line in plik:
            print(line, end="")

OperacjeNaPliku()