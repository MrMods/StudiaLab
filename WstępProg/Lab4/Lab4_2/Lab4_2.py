#Zad1

def KwadratLiczby(x):
    print(x * x)                #Oblicza kwadrat podanej liczby

'''
Podaj liczbe której chcesz obliczyć kwadrat: 5
25.0
'''

#KwadratLiczby(float(input("Podaj liczbe której chcesz obliczyć kwadrat: ")))



#Zad2
def OdwracanieStr(x):
    print(x[::-1])          #Odwaraca tekst
'''
Podaj tekst: asdf
fdsa
'''
#OdwracanieStr(str(input("Podaj tekst: ")))

#Zad3
def Powitanie(imie="Użytkownik",jezyk="polski"):
    if jezyk == "polski":                       #Sprawdza jaki jezyk jest podany
        print(f"Cześć, {imie}")
    elif jezyk == "angielski":
        print(f"Hello, {imie}")
    elif jezyk == "niemiecki":
        print(f"Guten Morgen, {imie}")
    else:
        print(f"Witaj {imie}")

'''
Podaj swoje imię: Krystian
Podaj język: angielski
Hello, Krystian

'''
#Powitanie(str(input("Podaj swoje imię: ")), str(input("Podaj język: ")))

#Zad4

def SredniaListyLiczb(Lista):
    srednia = sum(Lista) / len(Lista)       #Oblicza srednia liczb z listy
    print(f"Lista: {Lista}, Średnia liczb z listy: {srednia}")

ListaLiczb = [1,2,3,4]
#SredniaListyLiczb(ListaLiczb)

#Zad5

def BMI(waga, wzrost):
    bmi = round((waga / (wzrost * wzrost)) * 10000, 2)          #Obliczanie bmi
    print(f"Twoje BMI wynosi: {bmi}")
    match bmi:                              #Sprawdza bmi, jezeli spelnia warunek to wypisuje odpowiednia kategorie
        case bmi if bmi < 18.5:
            print("Niedowaga")
        case bmi if bmi > 18.5 and bmi < 24.9:
            print("Pożadana masa ciała")
        case bmi if bmi > 25 and bmi < 29.9:
            print("Nadwaga")
        case bmi if bmi > 30 and bmi < 34.9:
            print("Otylosc 1 stopnień")
        case bmi if bmi > 35 and bmi < 39.9:
            print("Otylosc 2 stopnień")
        case bmi if bmi > 40:
            print("Otylosc 3 stopnień")
'''

Podaj swoją wage: 75
Podaj swój wzrost: 165
Twoje BMI wynosi: 27.55
Nadwaga

'''
#BMI(float(input("Podaj swoją wage: ")), float(input("Podaj swój wzrost: ")))

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
'''
try:                                                                        #Sprawdzanie poprawnosci
    PoleTrojkata(float(input("Podaj bok a: ")),float(input("Podaj bok b: ")), float(input("Podaj bok c: ")))
except ValueError as ve:
    print("Error:", ve)
'''
'''
Podaj bok a: 3
Podaj bok b: 4
Podaj bok c: 5
6.0

Podaj bok a: -15
Podaj bok b: 15-d
Error: could not convert string to float: '15-d'

'''

#Zad7

def potega(a, n):
    if n == 0:                          #Sprawdzanie czy n jest 0 ( jesli tak to zwraca 1)
        return 1
    elif n < 0:                         #Spradznanie czy n jest mniejsze od 0( jesli tak to oblicza potega od -n
        return 1 / potega(a, -n)
    else:                               #W każdyn innym przypadku oblicza potege liczby n
        return a * potega(a, n-1)


#print(potega(float(input("Podaj liczbe: ")), float(input("Podaj ktory element(n): "))))

#Zad8

def liczbaparametow(*args):
    print("Parametry:")
    for arg in args:            #Petla bierze argumenty z args
        print(f"- {arg}")
    print(f"Wartość maksymalna parametrów to: {max(args)}")     #Sprawdza najwiekszy parametr

'''
Parametry:
- 1
- 6
- 8
- 4
Wartość maksymalna parametrów to: 8
'''
#liczbaparametow(1,6,8,4)

#Zad9

def Fibo(n):
    if n <= 1:              #Dla 0, 1 pisze 0, 1
        return n
    return Fibo(n-1) + Fibo(n-2)        #Dla liczb wiekszych od 1 pisze n wyraz ciagu fibonacciego

'''
Podaj n wyraz: 8
21
'''

#print(Fibo(int(input("Podaj n'ty wyraz: "))))

