"""
Created on 05-15-2019

@author: Johann Dolivet

Correction d'un algorithme
Calcul de (a * b) en n'effectuant que des multiplications et divisions par 10.
Invariant de boucle : z + x * y = a * b
"""

x = int(input("Entrez un entier a : "))
y = int(input("Entrez un entier b : "))
z = 0
invariant = z + x * y
while y != 0:
    z = z + x * (y % 10)
    x = 10 * x
    y = y // 10
print("Le résultat est : ", z)
