#Zad8

def liczbaparametow(*args):
    print("Parametry:")
    for arg in args:            #Petla bierze argumenty z args
        print(f"- {arg}")
    print(f"Wartość maksymalna parametrów to: {max(args)}")     #Sprawdza najwiekszy parametr

'''
Parametry:
- 1
- 6
- 8
- 4
Wartość maksymalna parametrów to: 8
'''
liczbaparametow(1,6,8,4)