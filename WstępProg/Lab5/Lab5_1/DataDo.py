import datetime

def ileuplynelo():
    data_laboratoriow = input("Podaj date ostatnich laboratoriow (d-m-r): ")
    data_laboratoriow = datetime.datetime.strptime(data_laboratoriow, "%d-%m-%Y")           #Podana date zamienia na format datetime()

    data_kolokwium = datetime.datetime(2025, 1, 19)                               #Zamienia podane wartosci na format datetime()
    data_dzisiaj = datetime.datetime.now()                                                        #Dzisiejsza data

    dni_od_laboratoriow = (data_dzisiaj - data_laboratoriow).days                                   #Oblicza ile dni uplynelo od laboratorow podanych przez uzytkownika

    dni_do_kolokwium = (data_kolokwium - data_dzisiaj).days                                      #Oblicza ile dni do kolokwium

    print(f"Od ostatnich laboratoriów upłyneło ({data_laboratoriow.date()}): {dni_od_laboratoriow} dni")            #Wypisanie dat
    print(f"Do kolokwium pozostalo ({data_kolokwium.date()}): {dni_do_kolokwium} dni")                               #Wypisanie dat

ileuplynelo()


'''
Podaj date ostatnich laboratoriow (d-m-r): 15-12-2024
Od ostatnich laboratoriów upłyneło (2024-12-15): 2 dni
Do kolokwium pozostalo (2025-01-19): 32 dni
'''