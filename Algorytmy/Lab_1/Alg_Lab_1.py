#Zad 1
import random
import copy
from wsgiref.util import request_uri


def RownanieKwadratowe(a,b,c):
    # 2. Obliczanie delty
    delta = (b**2) - (4*a*c)

   #3. Jezeli delta jest wieksza od 0
    if delta > 0:
        #3.1 Obliczenia
        x1 = (-b - delta**(1/2)) / (2*a)
        x2 = (-b + delta**(1/2)) / (2*a)
        print (f"x1 = {x1} x2 = {x2}")
    #4. Jezeli delta jest równa 0
    elif delta == 0:
        #4.1 Obliczenia
        x1 = -b / (2*a)
        print(f"x = {x1}")
    #5. Jezeli delta jest mniejsza od 0
    else:
        print("Brak rozwiązań")

#1. Wprowadzanie zmiennych
#RownanieKwadratowe(float(input("Podaj a: ")), float(input("Podaj b: ")), float(input("Podaj c: ")))

#Zad 2

def liczba_liczb_parzystych(n):
    #1.b. Sprawdzanie wprowadzenia poprawnej liczby
    if n <= 0:
        print("n musi być wieksze od 0")
        return
    #2.Utworzenie zmiennej l_parz
    l_parz = 0

    #3.Petla od i = 0 do n
    for i in range(n):
        #3.1 Wprowadzanie liczby x
        x = int(input(f"Podaj liczbe {i+1}: "))
        #3.2 Obliczanie parzystosli liczby, jezeli jest do zwieksza l_parz
        if x % 2 == 0:
            #Zwiekszanie ilosci liczb parzystych
            l_parz += 1
    #4. Wypisywanie ilosci liczb parzystych
    print(f"Ilosc liczby parzystych w ciągu: {l_parz}")

#1.Wprowadzenie liczby dlugosci ciagu
#liczba_liczb_parzystych(int(input("Podaj ilość liczb: ")))


#Zad 3

def liczba_w_ciagu(n):
    #1.b. Sprawdzanie wprowadzenia poprawnej liczby
    if n <= 0:
        print("n musi być wieksze od 0")
        return
    #2.Utworzenie pustego ciagu
    ciag = []
    #3. Podawanie, oraz dodawanie liczb do listy ciag
    for i in range(n):
        liczba = int(input(f"Podaj liczbe {i + 1}: "))
        ciag.append(liczba)
    #4. Podanie liczby do znalezienia w ciagu
    x = int(input(f"Podaj liczbe do znalezienia w ciagu: "))

    #5. Sprawdznie czy x jest w ciagu
    if x in ciag:
        #5.1 Wyswietlanie komunikatu, sprawdznie indeksu liczby
        index = ciag.index(x)
        print(f"Liczba {x} wystepuje w ciagu na pozycji o indeksie {index}")
    else:
        # 5.2 Wyswietlanie komunikatu
        print(f"Liczba {x} nie wystepuje w ciagu")

#1.Wprowadzenie liczby elementow ciagu
#liczba_w_ciagu(int(input("Podaj ilość liczb: ")))

#Zad 4
def zgadywanie_liczby():
    #1. Wybieranie losowej liczby
    liczba = random.randint(1,100)
    #2. Ustawianie licznika prob
    liczbnik_prob = 1
    print("Odgadnij liczbe z przedzialu 1-100")
    #3. Zgadywanie
    while True:
        try:
            #3. Podawanie liczby
            x = int(input("Podaj swoja liczbe: "))
            #3.1 Liczba rowna poszukiwanej, przejscie do punktu 4
            if x == liczba:
                print("Gratulacje odgadles wylosowana liczbe!!!")
                break
            #3.2 Liczba wieksza od poszukiwanej
            elif x > liczba:
                print("Liczba jest wieksza od wylosowanej liczby")
            #3.3 Liczba mniejsza od poszukiwanej
            else:
                print("Liczba jest mniejsza od wylosowanej liczby")
            #3.4 Zwiekszanie licznika prob
            liczbnik_prob += 1
            #3.5 Powrot do punktu 3
        except ValueError:
            print("Blad! Podaj liczbe calkowita.")
    #4. Komunikat o poprawnej liczbie
    print(f"Prawidłowa liczba to: {liczba}")
    #5. Komunikat o ilosci prob
    print(f"Odgadłeś liczbę w {liczbnik_prob} próbach!")
#zgadywanie_liczby()

#Zad 5

def druga_najwieksza(lista):
    szukana_liczba = sorted(set(lista), reverse=True)

    if len(szukana_liczba) < 2:
        print("Lista musi zawierac co najmniej dwie rozne liczby")
    else:
        print(f"Druga najwieksza wartosc w liscie wynosi {szukana_liczba[1]}")

lista1 = [10, 20, 4, 45, 99, 99]
lista2 = [1, 2, 3, 4, 5]
lista3 = [10, 10, 10, 9]
#druga_najwieksza(lista1)
#druga_najwieksza(lista2)
#druga_najwieksza(lista3)

#Zad 6

def znajdz_min_max(macierz):

    min_wartosc = float('inf')
    max_wartosc = float('-inf')
    min_poz = (0,0)
    max_poz = (0,0)

    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] < min_wartosc:
                min_wartosc = macierz[i][j]
                min_poz = (i,j)
            if macierz[i][j] > max_wartosc:
                max_wartosc = macierz[i][j]
                max_poz = (i,j)

    macierz_kopia = copy.deepcopy(macierz)

    i_min, j_min = min_poz
    i_max, j_max = max_poz

    macierz_kopia[i_min][j_min] = "MIN"
    macierz_kopia[i_max][j_max] = "MAX"

    for wiersz in macierz_kopia:
        print(wiersz)

macierz1 = [
    [5, 2, 9, 8],
    [1, 7, 3, 4],
    [6, 0, 2, 5]
]

#znajdz_min_max(macierz1)

#Zad 7
def tabelka():
    global licznik
    licznik = 0

    def wynik(i):
        global licznik
        licznik += 1
        if i < 5:
            return 2 # Zmieniona wartość bazowa
        elif i % 2 == 0: # Jeśli i jest parzyste
            return wynik(i - 4) + wynik(i - 2) + 2
        else: # Jeśli i jest nieparzyste
            return wynik(i - 2) % 9 # Zmieniona operacja mod


    for i in range(1,16):
        licznik = 0
        print(f"{i}: {wynik(i)}, {licznik-1}")

#tabelka()

#Zad 8

def czy_palindrom(napis):

    if len(napis) <= 1:
        return True
    if napis[0] != napis[-1]:
        return False
    return czy_palindrom(napis[1:-1])

print(czy_palindrom('kajak'))
print(czy_palindrom("kajak"))
print(czy_palindrom("radar"))
print(czy_palindrom("python"))
print(czy_palindrom("anna"))