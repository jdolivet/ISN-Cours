"""
Created on 03-23-2020

@author: Johann Dolivet

Module
Ce module contient quelques fonctions et constantes relatif au cercle...
On pourra ainsi l'importer depuis un autre programme.
"""

pi = 3.14159


def aire(R):
    """ Retourne l'aire d'un disque de rayon R """
    return pi * (R ** 2)


def perimetre(R):
    """ Retourne le périmètre d'un cercle de rayon R """
    return 2 * pi * R


def surfaceSphere(R):
    """ Retourne l'aire d'une sphère de rayon R """
    return 4 * aire(R)


def volumeBoule(R):
    """ Retourne le volume d'une boule de rayon R """
    return (4 / 3) * pi * (R ** 3)
