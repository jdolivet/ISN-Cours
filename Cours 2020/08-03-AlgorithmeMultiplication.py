"""
Created on 05-18-2020

@author: Johann Dolivet

Correction d'un algorithme
Calcul de (a * b) en n'effectuant que des additions.
Invariant de boucle : z + x * y = a * b
"""

x = int(input("Entrez un entier a : "))
y = int(input("Entrez un entier b : "))
z = 0
invariant = z + x * y
while y != 0:
    z = z + x
    y = y - 1
print("Le résultat est : ", z)
