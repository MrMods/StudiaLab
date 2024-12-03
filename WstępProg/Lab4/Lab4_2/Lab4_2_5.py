#Zad5

def BMI(waga, wzrost):
    bmi = round((waga / (wzrost * wzrost)) * 10000, 2)          #Obliczanie bmi
    print(f"Twoje BMI wynosi: {bmi}")
    match bmi:                              #Sprawdza bmi, jezeli spelnia warunek to wypisuje odpowiednia kategorie
        case bmi if bmi < 18.5:
            print("Niedowaga")
        case bmi if bmi > 18.5 and bmi < 24.9:
            print("Pożadana masa ciała")
        case bmi if bmi > 25 and bmi < 29.9:
            print("Nadwaga")
        case bmi if bmi > 30 and bmi < 34.9:
            print("Otylosc 1 stopnień")
        case bmi if bmi > 35 and bmi < 39.9:
            print("Otylosc 2 stopnień")
        case bmi if bmi > 40:
            print("Otylosc 3 stopnień")
'''

Podaj swoją wage: 75
Podaj swój wzrost: 165
Twoje BMI wynosi: 27.55
Nadwaga

'''
BMI(float(input("Podaj swoją wage: ")), float(input("Podaj swój wzrost: ")))