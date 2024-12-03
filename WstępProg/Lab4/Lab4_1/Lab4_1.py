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
##MojaLista()

#Zad2

def ListaImion():

    MyList=["krystian", "michal", "pawel", "adrianna"]

    print(sorted(MyList))                       #Sortuje wyrazy

    MyList.append("ola")                        #Dodaje wyraz ola
    MyList.append("lukasz")                     #Dodaje wyraz lukasz
    print(MyList.pop())                         #Pobiera ostatni wyraz

    MyList.insert(2, "Zuza")                #Dodaje na index 2 wyraz zuza
    print(MyList)

    MyList.reverse()                            #Odwraca liste
    MyList = MyList*2                           #Powtarza 2 razy liste
    print(MyList)

'''
['adrianna', 'krystian', 'michal', 'pawel']
lukasz
['krystian', 'michal', 'Zuza', 'pawel', 'adrianna', 'ola']
['ola', 'adrianna', 'pawel', 'Zuza', 'michal', 'krystian', 'ola', 'adrianna', 'pawel', 'Zuza', 'michal', 'krystian']
'''

##ListaImion()

#Zad3

def zmienne():
    imie = str(input("Podaj imie: "))
    print(f"Witaj {imie}")

    wiek = int(input("Podaj wiek: "))
    print(f"Twój wiek to: {wiek}")

    imie = str(input("Podaj imie: "))
    nazwisko = str(input("Podaj nazwisko: "))
    print(f"Inicjaly: {imie[0]}{nazwisko[0]}")              #Pobiera 1 litere z zmiennych

    lancuch = input("Podaj lancuch: ")
    for i in range(0, 5):                                   #Petla wykonuje sie 5 razy
        print(lancuch)

    lancuch1 = input("Podaj lancuch1: ")
    lancuch2 = input("Podaj lancuch2: ")
    lancuch3 = lancuch1 + lancuch2                          #Laczenie 2 lancuchow
    print(lancuch3)

    lancuch1 = input("Podaj lancuch1: ")
    lancuch2 = input("Podaj lancuch2: ")
    lancuch3 = lancuch1[:int(((len(lancuch1)) / 2))] + lancuch2[int(((len(lancuch2)) / 2)):]            #Pobiera 1 polowe z 1 lancuchu i 2 polowe z 2 lancuchu
    print(lancuch3)

'''
Podaj imie: Krystian
Witaj Krystian
Podaj wiek: 23
Twój wiek to: 23
Podaj imie: Krystian
Podaj nazwisko: Zadlo
Inicjaly: KZ
Podaj lancuch: Tata
Tata
Tata
Tata
Tata
Tata
Podaj lancuch1: Mam
Podaj lancuch2: Zadanie
MamZadanie
Podaj lancuch1: Wita
Podaj lancuch2: Moje
Wije
'''

##zmienne()

##Zad4

def wypisaywanieliter(zdanie):
    zdanie = zdanie.lower().replace(" ", "")        #Zamienia duze litery na male i usuwa spacje

    litery = sorted(set(zdanie))                    #Sortuje i usuwa powtarzajace sie litery (dzieki zbiorowi set)
    print(f"Litery w kolejnosci alfabetycsznej: {litery}")

    alfabet = list("abcdefghijklmnopqrstuvwxyz")
    brak_litery = [litera for litera in alfabet if litera not in litery]        #sprawdza kazda litere alfabetu czy znajduje sie w literach ze zdania, jesli litera nie znajduje sie w zdaniu dodaje do listy

    print(f"Brakujace litery alfabetu: {brak_litery}")

'''
Podaj zdanie: ala ma kota
Litery w kolejnosci alfabetycsznej: ['a', 'k', 'l', 'm', 'o', 't']
Brakujace litery alfabetu: ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'n', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
'''

#wypisaywanieliter(input("Podaj zdanie: "))



##Zad5
def krotka():
    dni = ("Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela")
    print(dni)

'''
('Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela')
'''
##krotka()

#Zad6
def elementykrotki():

    owoce = ('jabłko', 'banan', 'gruszka', 'banan', 'banan', 'malina')
    print(f"Liczba bananów w krotce to: {owoce.count('banan')}")             #Sprawdza ile bananow jest w krotce

'''
Liczba bananów w krotce: 3
'''

##elementykrotki()

#Zad7
def sortowaniekrotki():
    moja_krotka= (10, 2, 6, 6, 9, 13, 0,1)
    MyList = moja_krotka                    #Zamiennia krotke na liste
    moja_krotka = sorted(MyList)            #Sortuje liczby w liscie / zamienia liste na krotke
    print(moja_krotka)

'''
[0, 1, 2, 6, 6, 9, 10, 13]
'''

##sortowaniekrotki()

#Zad8
def stopnie():
    stopnie = ("Szeregowy", "Kapral", "Sierżancie", "Porucznik", "Kapitan", "Major", "Pułkownik",)

    ilosc_stopnii = len(stopnie)        #sprawdza ile jest stopni
    print(ilosc_stopnii)

    Major_index = stopnie.index('Major')                #Sprawdza czy jest index major w stopniach
    print(Major_index)

    Pułkownik_wstepowanie = 'Pułkownik' in stopnie              #Sprawdza czy wystepuje pulkownik w stopniach
    print(Pułkownik_wstepowanie)

'''
7
5
True
'''

##stopnie()

#Zad9
def listazakupowslownik():

    listazakupow = {'kawa': 5, 'maslo':3, 'chleb': 5}
    print(listazakupow)
    print(f"Wydatki: {sum(listazakupow.values())} zl")          #Sumuje wydatki z listy zakupow

'''
{'kawa': 5, 'maslo': 3, 'chleb': 5}
Wydatki: 13 zl
'''

##listazakupowslownik()