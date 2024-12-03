#Zad4

def SredniaListyLiczb(Lista):
    srednia = sum(Lista) / len(Lista)            #Oblicza srednia liczb z listy
    print(f"Lista: {Lista}, Średnia liczb z listy: {srednia}")

ListaLiczb = [1,2,3,4]
SredniaListyLiczb(ListaLiczb)