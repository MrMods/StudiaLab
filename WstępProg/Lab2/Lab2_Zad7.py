#Zad 7
def haslo():

    haslo = 'pk47!jy0893'

    if len(haslo) >= 11 and "!" in haslo:           #Sprawdzenie czy haslo jest dluzsze od 11 znakow oraz czy zawiera !
        print("Hasło jest poprawne")
    else:
        print("Hasło jest nie poprawne")

#Hasło jest poprawne

haslo()