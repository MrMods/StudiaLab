import pandas as pd
from unicodedata import decimal

df = pd.read_csv('demografia.csv', decimal=',',na_values=['NA', 'n/a', 'NaN'])

#print(df)

przyrost_max = df.iloc[:, 1:].max().max()                                                             #Wyszukuje wszystkie kolumny poza 0 (kraj), znajduje najwieksze wartosci we wszystkich kolumnach, nastepnie najwzysza ze znalezionych
przyrost_max_kraj = df.loc[df[df.iloc[:, 1:].max().idxmax()].idxmax(), "KRAJE"]                       #Wyszukuje index z najwieksza wartoscią(poza kolumna 0), wyszukuje kraj po tym indexie i ogranicza do KRAJE

print(f"Najwiekszy przyrost we wszystkich latach wynisi: {przyrost_max}, w kraju: {przyrost_max_kraj}")

'''
Najwiekszy przyrost we wszystkich latach wynisi: 7.23, w kraju: San Marino 
'''