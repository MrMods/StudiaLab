#Zad6
def Pentla():
    while True:                                         #Petla nieskonczona
        liczba = int(input("Podaj liczbe: "))           #Podawanie liczby
        if liczba < 0:                                  #Sprawdzanie czy liczba jest ujemna
            print("Liczba ujemna wychodze z pętli")
            break                                       #Wychodzenie z petli
Pentla()

'''
Podaj liczbe: 54
Podaj liczbe: 65
Podaj liczbe: 15
Podaj liczbe: -1
Liczba ujemna wychodze z pętli
'''