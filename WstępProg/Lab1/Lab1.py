#Zad1 a
#Typ wyniku działania: 1+2
from site import check_enableusersite

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

a = input("Bok a")
b = input("Bok b")