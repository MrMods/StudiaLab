#Zad6

def PoleTrojkata(a,b,c):
    if any(x <= 0 for x in (a,b,c)) :                                       #Sprawdzanie czy ktorys bok trojkata jest mniejszy od 0
        print("Długości boków muszą być wieksze niż zero")
        return
    elif not(a+b > c and a+c > b and b+c > a):                              #Sprawdzanie czy jest to rzeczywisty trojkat (jesli któreś wyrażenie jest falszywe to sie wykonuje warunek)
        print("Długości boków nie tworzą rzeczywistego trójkąta")
        return

    półobw = (a + b + c)/ 2                                                 #Obliczenia
    pole = (półobw * ( półobw - a) * (półobw - b) * (półobw - c))**(1/2)

    print(pole)

try:                                                                        #Sprawdzanie poprawnosci
    PoleTrojkata(float(input("Podaj bok a: ")),float(input("Podaj bok b: ")), float(input("Podaj bok c: ")))
except ValueError as ve:
    print("Error:", ve)

'''
Podaj bok a: 3
Podaj bok b: 4
Podaj bok c: 5
6.0

Podaj bok a: -15
Podaj bok b: 15-d
Error: could not convert string to float: '15-d'

'''