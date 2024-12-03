#Zad7
def sortowaniekrotki():
    moja_krotka= (10, 2, 6, 6, 9, 13, 0,1)
    MyList = moja_krotka                    #Zamiennia krotke na liste
    moja_krotka = sorted(MyList)            #Sortuje liczby w liscie / zamienia liste na krotke
    print(moja_krotka)

'''
[0, 1, 2, 6, 6, 9, 10, 13]
'''

sortowaniekrotki()