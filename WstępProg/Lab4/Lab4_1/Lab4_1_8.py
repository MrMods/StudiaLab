#Zad8
def stopnie():
    stopnie = ("Szeregowy", "Kapral", "Sierżancie", "Porucznik", "Kapitan", "Major", "Pułkownik",)

    ilosc_stopnii = len(stopnie)        #sprawdza ile jest stopni
    print(ilosc_stopnii)

    Major_index = stopnie.index('Major')                #Sprawdza czy jest index major w stopniach
    print(Major_index)

    Pułkownik_wstepowanie = 'Pułkownik' in stopnie              #Sprawdza czy wystepuje pulkownik w stopniach
    print(Pułkownik_wstepowanie)

'''
7
5
True
'''

stopnie()