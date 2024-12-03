##Zad4

def wypisaywanieliter(zdanie):
    zdanie = zdanie.lower().replace(" ", "")        #Zamienia duze litery na male i usuwa spacje

    litery = sorted(set(zdanie))                    #Sortuje i usuwa powtarzajace sie litery (dzieki zbiorowi set)
    print(f"Litery w kolejnosci alfabetycsznej: {litery}")

    alfabet = list("abcdefghijklmnopqrstuvwxyz")
    brak_litery = [litera for litera in alfabet if litera not in litery]        #sprawdza kazda litere alfabetu czy znajduje sie w literach ze zdania, jesli litera nie znajduje sie w zdaniu dodaje do listy

    print(f"Brakujace litery alfabetu: {brak_litery}")

'''
Podaj zdanie: ala ma kota
Litery w kolejnosci alfabetycsznej: ['a', 'k', 'l', 'm', 'o', 't']
Brakujace litery alfabetu: ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'n', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
'''

wypisaywanieliter(input("Podaj zdanie: "))