#Zad5
def ListaLiczb():
    listaliczb = []                     #Lista liczb
    for i in range(80, -1 , -4):        #Petla od 80 do 0 co 4 kroki
        listaliczb.append(i)            #Dodawanie do listy liczb

    print(listaliczb)

ListaLiczb()

'''
[80, 76, 72, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4, 0]
'''