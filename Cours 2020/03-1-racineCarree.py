"""
Created on 03-02-2020

@author: Johann Dolivet

Exhaustivité (check and guess)

Retourne la valeur approchée de la racine carrée de x à une précision epsilon
"""

x = 25
epsilon = 0.01
step = epsilon ** 2
nbEssais = 0
ans = 0.0
while (abs(ans ** 2 - x) >= epsilon) and (ans * ans <= x):
    ans += step
    nbEssais += 1
print("Nombre d'essais =", nbEssais)
if abs(ans ** 2 - x) >= epsilon:
    print("Raté pour la racine carrée de", x)
else:
    print(ans, "est proche de racine carrée de", x)
