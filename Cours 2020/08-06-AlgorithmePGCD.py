"""
Created on 05-18-2020

@author: Johann Dolivet

Calcul du PGCD de a et b
Algorithme d'Euclide
Fonction dans sa version récursive
"""

def pgcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return pgcd(b, r)
