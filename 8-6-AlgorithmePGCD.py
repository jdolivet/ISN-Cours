"""
Created on 05-15-2019

@author: Johann Dolivet

Calcul du PGCD de a et b
Algorithme des soustractions
Débogage
"""

a = int(input("Choisir l'entier a : "))
b = int(input("Choisir l'entier b : "))
d = a - b
while d != 0:
    a = b
    print("a = " + str(a), end =' ')
    b = d
    print("b = " + str(b), end =' ')
    d = a - b
    print("d = " + str(d))
print("Le PGCD est ", b)
