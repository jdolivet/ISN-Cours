"""
Created on 05-15-2019

@author: Johann Dolivet

Calcul du PGCD de a et b
Algorithme des soustractions
Version finale
"""

a = int(input("Choisir l'entier a : "))
b = int(input("Choisir l'entier b : "))
d = a - b
while d != 0:
    if b < d:
        b, d = d, b
    a = b
    b = d
    d = a - b
print("Le PGCD est ", b)
