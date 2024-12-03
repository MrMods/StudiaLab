#Zad2

def ListaImion():

    MyList=["krystian", "michal", "pawel", "adrianna"]

    print(sorted(MyList))                       #Sortuje wyrazy

    MyList.append("ola")                        #Dodaje wyraz ola
    MyList.append("lukasz")                     #Dodaje wyraz lukasz
    print(MyList.pop())                         #Pobiera ostatni wyraz

    MyList.insert(2, "Zuza")                #Dodaje na index 2 wyraz zuza
    print(MyList)

    MyList.reverse()                            #Odwraca liste
    MyList = MyList*2                           #Powtarza 2 razy liste
    print(MyList)

'''
['adrianna', 'krystian', 'michal', 'pawel']
lukasz
['krystian', 'michal', 'Zuza', 'pawel', 'adrianna', 'ola']
['ola', 'adrianna', 'pawel', 'Zuza', 'michal', 'krystian', 'ola', 'adrianna', 'pawel', 'Zuza', 'michal', 'krystian']
'''

ListaImion()