import random

def DuzyLotek():
    Kule = []
    for i in range(1,50):
        Kule.append(i)                  #dodawanie kul od 1 do 49 do listy
    print(random.sample(Kule, k=6))         #Losowanie z listy 6 kul

DuzyLotek()


'''
[30, 28, 47, 26, 4, 13]
'''