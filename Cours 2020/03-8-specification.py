"""
Created on 03-02-2020

@author: Johann Dolivet

Fonctions

Utilisation des docstring
"""


def racineCarre(x, epsilon):
    """ x et epsilon sont int ou float, x >= 0 et epsilon > 0.
    Retourne un float y tel que y ** 2 soit à une distance \
inférieure à epsilon de x."""
    low = 0.0
    high = max(1.0, x)  # On traite le cas ou x<1.0 auquel cas x<sqrt(x)
    ans = (low + high) / 2
    while (abs(ans ** 2 - x) >= epsilon):
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2
    return ans