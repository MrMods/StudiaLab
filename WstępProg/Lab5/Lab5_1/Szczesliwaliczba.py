import random


def TwojaSzczesliwaLiczba():
    return print(f"Twoja szczęśliwa liczba: {random.randint(0,100)}")           #LOsowanie liczby z przedzialu

TwojaSzczesliwaLiczba()

ListaRocznikow = ["2001", "2002", "2003", "2004", "2005", "2000", "1999","1998"]

def SzczesliwyRocznik(Roczniki):
    return random.choice(Roczniki)              #Losowanie rocznika z listy rocznikow

print(f"Szczęśliwy rocznik to: {SzczesliwyRocznik(ListaRocznikow)}")



'''
Twoja szczęśliwa liczba: 90
Szczęśliwy rocznik to: 1999
'''