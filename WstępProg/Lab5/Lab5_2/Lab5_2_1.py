import pandas as pd
from unicodedata import decimal

df = pd.read_csv('demografia.csv', decimal=',',na_values=['NA', 'n/a', 'NaN'])

print(df)

maxliczba = df['2022'].idxmax(skipna=True)
krajmax = df.loc(maxliczba, "KRAJE")
print(maxliczba)
print(krajmax)
