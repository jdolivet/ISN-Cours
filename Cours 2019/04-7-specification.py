"""
Created on 03-13-2019

@author: Johann Dolivet

Fonctions

Tests pour une fonction
"""


def chercheRacine(x, puissance, epsilon):
    """ x et epsilon sont int ou float, puissance est un entier, \
epsilon > 0 et puissance >= 1.
    Retourne un float y tel que y ** puissance soit à une distance \
inférieure à epsilon de x.
    Si y n'existe pas, la fonction retourne None."""
    if x < 0 and puissance % 2 == 0:
        return None
    low = min(-1, x)
    high = max(1, x) 
    ans = (low + high) / 2
    while (abs(ans ** puissance - x) >= epsilon):
        if ans ** puissance < x:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2
    return ans


def testChercheRacine():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for puissance in range(1, 4):
            print("Test pour x = " + str(x) + " et puissance = " + \
                  str(puissance))
            resultat = chercheRacine(x, puissance, epsilon)
            if resultat == None:
                print("    Pas de racine")
            else:
                print("   ",resultat ** puissance, "~=", x)
