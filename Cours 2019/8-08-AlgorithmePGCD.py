"""
Created on 05-15-2019

@author: Johann Dolivet

Calcul du PGCD de a et b
Algorithme d'Euclide
"""

a = int(input("Choisir l'entier a : "))
b = int(input("Choisir l'entier b : "))
r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
print("Le PGCD est ", b)
