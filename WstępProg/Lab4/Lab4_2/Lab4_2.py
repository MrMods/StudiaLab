#Zad1

def KwadratLiczby(x):
    print(x * x)

'''
Podaj liczbe której chcesz obliczyć kwadrat: 5
25.0
'''

#KwadratLiczby(float(input("Podaj liczbe której chcesz obliczyć kwadrat: ")))



#Zad2
def OdwracanieStr(x):
    print(x[::-1])
'''
Podaj tekst: asdf
fdsa
'''
#OdwracanieStr(str(input("Podaj tekst: ")))

#Zad3
def Powitanie(imie="Użytkownik",jezyk="polski"):
    if jezyk == "polski":
        print(f"Cześć, {imie}")
    elif jezyk == "angielski":
        print(f"Hello, {imie}")
    elif jezyk == "niemiecki":
        print(f"Guten Morgen, {imie}")
    else:
        print(f"Witaj {imie}")

'''
Podaj swoje imię: Krystian
Podaj język: angielski
Hello, Krystian

'''
#Powitanie(str(input("Podaj swoje imię: ")), str(input("Podaj język: ")))

#Zad4

def SredniaListyLiczb():
    Lista =[]
    def PodawanieLiczb(x):
        Lista.append(x)


SredniaListyLiczb(float(input("Podaj swoje imię: ")))


