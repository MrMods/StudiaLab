import time

def Sekundnik():
    czas = int(input("Podaj liczbę sekund do odliczenia: "))                #Podawanie czasu
    if czas < 0:                                                            #Sprawdzanie czy czas jest mniejszy od 0
        print("Liczba sekund musi być większa od 0")
        return
    while czas >= 0:                                                        #Petla odliczajaca czas co 1 sekune
        print(f"Pozostały czas to: {czas} sekund")
        time.sleep(1)
        czas -= 1

    print("Czas minął!!!")

Sekundnik()


'''
Podaj liczbę sekund do odliczenia: 5    
Pozostały czas to: 5 sekund
Pozostały czas to: 4 sekund
Pozostały czas to: 3 sekund
Pozostały czas to: 2 sekund
Pozostały czas to: 1 sekund
Pozostały czas to: 0 sekund
Czas minął!!!

'''