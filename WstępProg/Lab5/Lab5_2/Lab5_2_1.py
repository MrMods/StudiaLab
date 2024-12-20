import pandas as pd
from unicodedata import decimal

df = pd.read_csv('demografia.csv', decimal=',',na_values=['NA', 'n/a', 'NaN'])

print(df)

