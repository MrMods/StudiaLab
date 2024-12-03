#Zad9
def listazakupowslownik():

    listazakupow = {'kawa': 5, 'maslo':3, 'chleb': 5}
    print(listazakupow)
    print(f"Wydatki: {sum(listazakupow.values())} zl")          #Sumuje wydatki z listy zakupow

'''
{'kawa': 5, 'maslo': 3, 'chleb': 5}
Wydatki: 13 zl
'''

listazakupowslownik()