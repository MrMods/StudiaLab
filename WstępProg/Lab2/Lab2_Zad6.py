#Zad 6

def SprawdzanieDuzejLitery(litera):

   if litera.isalpha() and len(litera) == 1:                #Sprawdzenie czy jest jedna litera
       if litera.isupper():                                 #Sprawdzenie czy jest duza litera
           print(f"Litera: {litera} jest dużą literą.")
       else:
           print(f"Litera: {litera} jest małą literą.")     #Sprawdzenie czy jest mala
   else:
       print("Wprowadzony znak nie jest pojedynczą literą.")

SprawdzanieDuzejLitery(input("Podaj litere: "))

'''
Podaj litere: D
Litera: D jest dużą literą.

'''