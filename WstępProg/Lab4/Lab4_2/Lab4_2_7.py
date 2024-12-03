#Zad7

def potega(a, n):
    if n == 0:                          #Sprawdzanie czy n jest 0 ( jesli tak to zwraca 1)
        return 1
    elif n < 0:                         #Spradznanie czy n jest mniejsze od 0( jesli tak to oblicza potega od -n
        return 1 / potega(a, -n)
    else:                               #W każdyn innym przypadku oblicza potege liczby n
        return a * potega(a, n-1)


print(potega(float(input("Podaj liczbe: ")), float(input("Podaj ktory element(n): "))))