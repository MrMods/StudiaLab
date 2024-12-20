import f_mat                        #Import modulu f_mat

print(f"A)Kwadrat liczby: {f_mat.kwadrat(10)}")         #Wywolywanie funkcji z modulu
print(f"A)Szescian liczby: {f_mat.szescian(3)}")
print(f"A)Dodawanie liczb: {f_mat.dodaj(10,5)}")

from f_mat import kwadrat                               #Import konkretnych funkcji z modulu
from f_mat import szescian
from f_mat import dodaj

print(f"B)Kwadrat liczby: {kwadrat(10)}")
print(f"B)Kwadrat liczby: {szescian(3)}")
print(f"B)Kwadrat liczby: {dodaj(10,5)}")


'''
A)Kwadrat liczby: 100
A)Szescian liczby: 27
A)Dodawanie liczb: 15
B)Kwadrat liczby: 100
B)Kwadrat liczby: 27
B)Kwadrat liczby: 15
'''