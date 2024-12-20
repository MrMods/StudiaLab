import pandas as pd

data = {
    'ID': [1,2,3,4,5],
    'Imie': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35,28,40,30,45],
    'Pensja': [8000,4500,6000,5500,7000]
}

df = pd.DataFrame(data)

pensja = df[df['Pensja'] > 5000]                          #Z kolumny Pensja szuka wartosci wiekszych od 5000
print("Pracownicy z pensja wieksza od 5000 PLN:")
print(pensja, '\n')

sortowanie = df.sort_values(by='Wiek')                      #Sortuje wartosci wedłud wieku
print("Pracownicy posortowani po wieku:")
print(sortowanie, '\n')

grupowanie = df.groupby('Stanowisko')['Pensja'].mean()              #Grupuje pracownikow po stanowisku i oblicza srednia(mean)
print("Srednia pensja wedlug stanowiska pracownika:")
print(grupowanie, '\n')

zmiana_stanowiska = pd.DataFrame({                                      #Tworzenie nowej tabeli
    'ID': [2,4],
    "Nowe Stanowisko": ['Senior Programista', "Senior Programista"]
})

laczenie_tabel = pd.merge(df, zmiana_stanowiska, on="ID", how="left")                 #Laczenie tabel on - po jakim elemencie na laczyc tabele, how - rodzaj laczenia
print("Tabela po zmianie stanowisk pracowników:")
print(laczenie_tabel, '\n')

df.to_csv('pracownicy.csv', index= False)               #Zapisywanie do pliku csv

pracownicy_csv = pd.read_csv('pracownicy.csv')                    #Wczytywanie z pliku csv
print("Tabela wczytana z pliku CSV:")
print(pracownicy_csv)


'''
Pracownicy z pensja wieksza od 5000 PLN:
   ID       Imie    Nazwisko   Stanowisko  Wiek  Pensja
0   1       Anna    Kowalska      Manager    35    8000
2   3  Katarzyna  Wiśniewska   Konsultant    40    6000
3   4     Tomasz   Kaczmarek  Programista    30    5500
4   5     Michał   Zieliński      Manager    45    7000 

Pracownicy posortowani po wieku:
   ID       Imie    Nazwisko   Stanowisko  Wiek  Pensja
1   2        Jan       Nowak  Programista    28    4500
3   4     Tomasz   Kaczmarek  Programista    30    5500
0   1       Anna    Kowalska      Manager    35    8000
2   3  Katarzyna  Wiśniewska   Konsultant    40    6000
4   5     Michał   Zieliński      Manager    45    7000 

Srednia pensja wedlug stanowiska pracownika:
Stanowisko
Konsultant     6000.0
Manager        7500.0
Programista    5000.0
Name: Pensja, dtype: float64 

Tabela po zmianie stanowisk pracowników:
   ID       Imie    Nazwisko   Stanowisko  Wiek  Pensja     Nowe Stanowisko
0   1       Anna    Kowalska      Manager    35    8000                 NaN
1   2        Jan       Nowak  Programista    28    4500  Senior Programista
2   3  Katarzyna  Wiśniewska   Konsultant    40    6000                 NaN
3   4     Tomasz   Kaczmarek  Programista    30    5500  Senior Programista
4   5     Michał   Zieliński      Manager    45    7000                 NaN 

Tabela wczytana z pliku CSV:
   ID       Imie    Nazwisko   Stanowisko  Wiek  Pensja
0   1       Anna    Kowalska      Manager    35    8000
1   2        Jan       Nowak  Programista    28    4500
2   3  Katarzyna  Wiśniewska   Konsultant    40    6000
3   4     Tomasz   Kaczmarek  Programista    30    5500
4   5     Michał   Zieliński      Manager    45    7000
'''