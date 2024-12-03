#Zad3
def Powitanie(imie="Użytkownik",jezyk="polski"):
    if jezyk == "polski":                       #Sprawdza jaki jezyk jest podany
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
Powitanie(str(input("Podaj swoje imię: ")), str(input("Podaj język: ")))