"""
Created on 05-15-2019

@author: Johann Dolivet

Calcul du PGCD de a et b
Algorithme d'Euclide
Fonction dans sa version itérative
"""

def pgcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b
