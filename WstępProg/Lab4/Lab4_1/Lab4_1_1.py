#Zad1
def MojaLista():

    Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
    print(Moja_lista[1])                #pobiera 2 wyraz
    print(Moja_lista[-1])               #pobiera ostatni wyraz
    print(len(Moja_lista))              #sprawdza dlugosci listy
    print(max(Moja_lista))              #sprawdza najwiekszy wyraz
    print(sum(Moja_lista))              #Suma wyrazow listy
    print(sorted(Moja_lista))           #Sortuje wyrazy w liscie

    Moja_lista.append(41)               #Dodaje do listy 41
    print(Moja_lista)

    Moja_lista.reverse()                #Odwraca liste
    print(Moja_lista)

'''
17
21
10
90
232
[1, 2, 3, 3, 4, 5, 17, 21, 86, 90]
[1, 17, 3, 5, 3, 4, 86, 90, 2, 21, 41]
[41, 21, 2, 90, 86, 4, 3, 5, 3, 17, 1]
'''
MojaLista()
