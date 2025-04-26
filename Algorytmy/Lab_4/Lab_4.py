#Zad 1
def odwrotnoscstosu():
    stos = []

    liczby = input("Podaj ciąg liczb całkowitych oddzielonych spacją: ").split()

    for liczba in liczby:
        stos.append(int(liczba))

    print("Liczy w odwróconej kolejności")
    while stos:
        print(stos.pop(), end=" ")

#odwrotnoscstosu()

#Zad 2

def sprnawiasow(wyrazenie):
    stos = []

    for znak in wyrazenie:
        if znak == "(":
            stos.append(znak)
        elif znak == ")":
            if not stos:
                return False
            stos.pop()
    return len(stos) == 0 #Jeśli stos jest pusty, nawiasy są poprawnie zapisane

#testy = ["()",")()","(","()()"]
#for test in testy:
#    print(f'{test}:' 'Poprawny' if sprnawiasow(test) else 'Błąd')

#Zad 3

def symcofania():
    stos = []


        tekst = input("Podaj tekst do zapisu: ")




