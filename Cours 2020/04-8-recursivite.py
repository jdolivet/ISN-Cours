"""
Created on 03-23-2020

@author: Johann Dolivet

Fonctions

Récursivité
"""


def factR(n):
    """ On suppose que n est un int > 0
    Retourne n!"""
    if n==1:
        return 1
    else:
        return n * factR(n-1)
