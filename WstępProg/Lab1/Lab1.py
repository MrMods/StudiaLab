import random


#Zad1 a
#Typ wyniku działania: 1+2
a= 1+2
print(type(a))
#<class 'int'>
#Typ wyniku działania: 1 + 4.5
a= 1 + 4.5
print(type(a))
#<class 'float'>
#Typ wyniku działania: 3 / 2
a= 3 / 2
print(type(a))
#<class 'float'>
# #Typ wyniku działania: 4 / 2
a= 4 / 2
print(type(a))
#<class 'float'>
# #Typ wyniku działania: 3 // 2
a= 3 // 2
print(type(a))
#<class 'int'>
#Typ wyniku działania: -3 // 2
a= -3 // 2
print(type(a))
#<class 'int'>
#Typ wyniku działania: 11 % 2
a= 11 % 2
print(type(a))
#<class 'int'>
#Typ wyniku działania: 2 ** 10
a= 2 ** 10
print(type(a))
#<class 'int'>
#Typ wyniku działania: 8 ** (1/3)
a= 8 ** (1/3)
print(type(a))
#<class 'float'>

#Zad 1 b
print(int(3.0))
#Zamiana liczby zmiennoprzecinkowej na całkowitą
print(float(3))
#Zamiana liczby całkowitej na zmiennoprzecinkową
print(float("3"))
#Zamiana testu na zmiennoprzecinkową
print(str(12.4))
#Zamiana liczby zmiennoprzecinkowej na tekst
print(bool(0))
#Zamiana liczby całkowitej na typ danych logicznych

#Zad2

uczelnia = "Studiuję na WSIiZ"
print(uczelnia)
#Studiuję na WSIiZ

#Zad3
imię = "Jan"
wiek = 20
wzrost = 178
print("Nazywam się", imię, "i mam", wiek, "lat")
print("Mój wzrost to", wzrost, "cm")
#Nazywam się Jan i mam 20 lat
#Mój wzrost to 178 cm

#Zad4

cena = 39.99
rabat = 0.2

zrabatem = cena - (cena * rabat)

print(round(zrabatem,2))
#31.99

#Zad5

a = input("Podaj bok a: ")
b = input("Podaj bok b: ")

#Obliczenia
pole = int(a) * int(b)
obwod = 2*int(a) + 2*int(b)

print ("Pole prostokąta:",pole,"Obwód prostokąta:", obwod)

'''
Podaj bok a: 2
Podaj bok b: 3
Pole prostokąta: 6 Obwód prostokąta: 10
'''

#Zad6

#droga = input("Podaj drogę pokonaną przez samochód: ")
#cena = 6.5

droga = random.randint(1,1000)                   #Losuje liczbe z przedziału
spalanie = input("Podaj średne spalanie samochodu (l/100km): ")
cena = input("Podaj aktualną cena paliwa za litr: ")
zuzyciepaliwa = int(droga) / float(spalanie)            #Obliczanie zużycia paliwa

#print ("Przewidywanie zużycie paliwa: ", round(zuzyciepaliwa,2), "l.")
#print ("Szacowane koszty podróży: ", round(zuzyciepaliwa * float(cena),2),"zł.")

print(f"Przewidywanie zużycie paliwa: {round(zuzyciepaliwa,2)} l.")
print(f"Szacowane koszty podróży: {round(zuzyciepaliwa * float(cena))} zł.")

#Zad 7
def RownanieLinowe(x,y):
    a = float(x)            #Zamiania str na float
    b = float(y)            #Zamiania str na float

    #Sprawdzanie warunków dla rownania liniowego
    if a != 0:
        x = round(-b/a,2)
        print(f"x = {x}")
    elif a == 0 and b != 0:
        print("Równanie sprzeczne")
    else:
        print("Równanie tożsamościowe")


RownanieLinowe(input("Podaj ax: "),input("Podaj b: "))  #Wprowadzanie zmiennych do funkcji RownanieLinowe

#Zad8
def RownanieKwadratowe(x,y,z):
    a = float(x)            #Zamiania str na float
    b = float(y)            #Zamiania str na float
    c = float(z)            #Zamiania str na float

    delta = (b**2) - (4*a*c)        #Obliczanie delty

   #Sprawdzanie warunków dla równania kwadratowego
    if delta > 0:
        x1 = (-b - delta**(1/2)) / (2*a)
        x2 = (-b + delta**(1/2)) / (2*a)
        print (f"x1 = {x1} x2 = {x2}")
    elif delta == 0:
        x1 = -b / (2*a)
        print(f"x = {x1}")
    else:
        print("Brak rozwiązań")

RownanieKwadratowe(input("Podaj a: "), input("Podaj b: "), input("Podaj c: "))           #Wprowadzanie zmiennych do funkcji

#Zad9
def kalkulator(x,y):
    a = int(x)              #Zamiania str na int
    b = int(y)              #Zamiania str na int

    #Obliczenia
    dodawanie = a + b
    odejmowanie = a - b
    mnozenie = a * b
    dzielenie = round(a / b, 2)
    potegowanie = a ** b

    print (f"Wyniki:\n Dodawanie: {dodawanie}\n Odejmowanie: {odejmowanie}\n Mnożenie: {mnozenie}\n Dzielenie: {dzielenie}\n Potęgowanie: {potegowanie}")


kalkulator(input("Podaj pierwszą liczbę: "),input("Podaj drugą liczbę: "))      #Wprowadzenie zmiennych do funkcji kalkulator

'''
Wyniki:
 Dodawanie: 11
 Odejmowanie: -1
 Mnożenie: 30
 Dzielenie: 0.83
 Potęgowanie: 15625
 '''