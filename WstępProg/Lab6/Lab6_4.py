import numpy as np

#Zad 4
def ndLista():
    Liczby2 = [128,64,32,16,8,4,2,1]
    LiczbyBin = [1,1,0,0,1,0,1,1]

    wagi = np.array(Liczby2)
    liczba_bin = np.array(LiczbyBin)

    def wartosc_liczby_bin():
        LiczbaDziesietna = 0
        for i in range(0,8):                    #Sprawdzanie kazdej liczby w tablicy
            spr_bin = liczba_bin[i] == 1        #Sprawdzanie czy liczba w tablicy jest 1
            if spr_bin:
                LiczbaDziesietna += Liczby2[i]      #Dodanie liczby z wagi do liczby dziesietnej
        return LiczbaDziesietna

    print(f"Wartość liczby binarnej zamienionej na dziesiętną = {wartosc_liczby_bin()}")


'''
Wartość liczby binarnej zamienionej na dziesiętną = 203
'''

ndLista()

