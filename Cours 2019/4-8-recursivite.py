"""
Created on 03-13-2019

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
