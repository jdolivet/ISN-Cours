"""
Created on 05-11-2020

@author: Johann Dolivet

Utilisation des listes
Ce programme met en évidence les dangers lors de manipulation de listes.
La première fonction ne produit pas le résultat escompté.
Les manipulations de listes produisent des effets de bord.
"""


def enleveDouble(l1, l2):
    """On suppose que l1 et l2 sont des listes
    Retire les éléments de l1 qui sont dans l2"""
    for e1 in l1:
        if e1 in l2:
            l1.remove(e1)


# Ci dessous le programme corrigé
def enleveDoubleCorrection(l1, l2):
    """On suppose que l1 et l2 sont des listes
    Retire les éléments de l1 qui sont dans l2"""
    for e1 in l1[:]:    # il faut effectuer une copie de la liste parcourue
        if e1 in l2:
            l1.remove(e1)
