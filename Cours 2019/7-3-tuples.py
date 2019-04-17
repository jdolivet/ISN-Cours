"""
Created on 04-17-2019

@author: Johann Dolivet

Utilisation des tuples
"""


def chercheDiviseurs(n1, n2):
    """On suppose que n1 et n2 sont des entiers positifs
    Retourne un tuple contenant les diviseurs communs à n1 et n2"""
    diviseurs = ()
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            diviseurs = diviseurs + (i,)
    return diviseurs


def chercheDiviseursExtremes(n1, n2):
    """On suppose que n1 et n2 sont des entiers positifs
    Retourne un tuple contenant le plus petit diviseur commun autre que un
    et le PGCD"""
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if minVal == None or i < minVal:
                minVal = i
            if maxVal == None or i > maxVal:
                maxVal = i
    return (minVal, maxVal)
