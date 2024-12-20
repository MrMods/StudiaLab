import pandas as pd
from unicodedata import decimal

df = pd.read_csv('demografia.csv', decimal=',',na_values=['NA', 'n/a', 'NaN'])


kraj_przyrost_max = df.loc[df['2022'].idxmax(skipna=False), "KRAJE"]            #Wyszukuje index z najwieksza wartoscią, Loc- wyszukuje kraj pod tym indexem, na końcu ogranicza do KRAJE


print(f"Kraj z najwiekszym przyrostem w 2022 roku: {kraj_przyrost_max}")


'''
Kraj z najwiekszym przyrostem w 2022 roku: Malta
'''