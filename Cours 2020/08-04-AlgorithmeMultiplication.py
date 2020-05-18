"""
Created on 05-18-2020

@author: Johann Dolivet

Correction d'un algorithme
Calcul de (a * b) en n'effectuant que des multiplications et divisions par 2.
Invariant de boucle : z + x * y = a * b
"""

x = int(input("Entrez un entier a : "))
y = int(input("Entrez un entier b : "))
z = 0
invariant = z + x * y
while y != 0:
    if y % 2 == 1:
        z = z + x
    x = 2 * x
    y = y // 2
print("Le résultat est : ", z)
