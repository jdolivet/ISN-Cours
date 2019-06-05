"""
Created on 02-20-2019

@author: Johann Dolivet

Dichotomie
https://fr.wikipedia.org/wiki/Recherche_dichotomique

Retourne la valeur approchée de la racine carrée de x à une précision epsilon
"""

x = 25
epsilon = 0.01
step = epsilon ** 2
nbEssais = 0
low = 0.0
high = max(1.0, x)  # On traite le cas ou x<1.0 auquel cas x<sqrt(x)
ans = (low + high) / 2
while (abs(ans ** 2 - x) >= epsilon):
    print("min =", low,"max =", high, "réponse = ", ans)
    nbEssais += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2
print("Nombre d'essais =", nbEssais)
print(ans, "est proche de racine carrée de", x)
