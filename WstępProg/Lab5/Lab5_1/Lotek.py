import random

def DuzyLotek():
    Kule = []
    for i in range(1,50):
        Kule.append(i)
    print(random.sample(Kule, k=6))

DuzyLotek()
