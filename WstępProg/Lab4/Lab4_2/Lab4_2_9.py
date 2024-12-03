#Zad9

def Fibo(n):
    if n <= 1:              #Dla 0, 1 pisze 0, 1
        return n
    return Fibo(n-1) + Fibo(n-2)        #Dla liczb wiekszych od 1 pisze n wyraz ciagu fibonacciego

'''
Podaj n wyraz: 8
21
'''

print(Fibo(int(input("Podaj n'ty wyraz: "))))