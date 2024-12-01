#Zad1
def MojaLista():

    Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
    print(Moja_lista[1])
    print(Moja_lista[-1])
    print(len(Moja_lista))
    print(max(Moja_lista))
    print(sum(Moja_lista))
    print(sorted(Moja_lista))

    Moja_lista.append(41)
    print(Moja_lista)

    Moja_lista.reverse()
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

    print(sorted(MyList))

    MyList.append("ola")
    MyList.append("lukasz")
    print(MyList.pop())

    MyList.insert(2, "Zuza")
    print(MyList)

    MyList.reverse()
    MyList = MyList*2
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
    print(f"Inicjaly: {imie[0]}{nazwisko[0]}")

    lancuch = input("Podaj lancuch: ")
    for i in range(0, 5):
        print(lancuch)

    lancuch1 = input("Podaj lancuch1: ")
    lancuch2 = input("Podaj lancuch2: ")
    lancuch3 = lancuch1 + lancuch2
    print(lancuch3)

    lancuch1 = input("Podaj lancuch1: ")
    lancuch2 = input("Podaj lancuch2: ")
    lancuch3 = lancuch1[:int(((len(lancuch1)) / 2))] + lancuch2[:int(((len(lancuch2)) / 2))]
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
Podaj lancuch1: Domek
Podaj lancuch2: Jakis
DoJa
'''

##zmienne()

##Zad4

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
    print(f"Liczba bananów w krotce to: {owoce.count('banan')}")

'''
Liczba bananów w krotce: 3
'''

##elementykrotki()

#Zad7
def sortowaniekrotki():
    moja_krotka= (10, 2, 6, 6, 9, 13, 0,1)
    MyList = moja_krotka
    moja_krotka = sorted(MyList)
    print(moja_krotka)

'''
[0, 1, 2, 6, 6, 9, 10, 13]
'''

##sortowaniekrotki()

#Zad8
def stopnie():
    stopnie = ("Szeregowy", "Kapral", "Sierżancie", "Porucznik", "Kapitan", "Major", "Pułkownik",)

    ilosc_stopnii = len(stopnie)
    print(ilosc_stopnii)

    Major_index = stopnie.index('Major')
    print(Major_index)

    Pułkownik_wstepowanie = 'Pułkownik' in stopnie
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
    print(f"Wydatki: {sum(listazakupow.values())} zl")

'''
{'kawa': 5, 'maslo': 3, 'chleb': 5}
Wydatki: 13 zl
'''

##listazakupowslownik()