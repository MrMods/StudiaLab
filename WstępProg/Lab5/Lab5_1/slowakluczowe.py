import keyword

def SlowoKluczowe():
    Lista_Slow = ["for", "print", "break", "done", "bad"]                                                               #Lista Słów

    for i in range(0, len(Lista_Slow)):                                                                                 #Sprawdzanie kazdego słowa z listy
        wynik = "jest słowem kluczowym." if keyword.iskeyword(Lista_Slow[i])  else "nie jest słowem kluczowym."         #Sprawdzanie czy słowo jest słowem kluczowym
        print(f"Słowo '{Lista_Slow[i]}' {wynik}")                                                                       #Wypisanie wyniku



SlowoKluczowe()


'''
Słowo 'for' jest słowem kluczowym.
Słowo 'print' nie jest słowem kluczowym.
Słowo 'break' jest słowem kluczowym.
Słowo 'done' nie jest słowem kluczowym.
Słowo 'bad' nie jest słowem kluczowym.

'''