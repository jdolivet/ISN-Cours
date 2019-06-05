"""
Created on 05-15-2019

@author: Johann Dolivet

Calcul du PGCD de a et b
Recherche exhaustive
"""

a = int(input("Choisir l'entier a : "))
b = int(input("Choisir l'entier b : "))
if b > a:
    a, b = b, a
d = 1
pgcd = d
while d <= b:
    d = d + 1
    r1 = a % d
    r2 = b % d
    if r1 == 0 and r2 == 0:
        pgcd = d
print("Le PGCD de", a, "et", b, " est ", pgcd)
