"""
Created on 02-13-2019

@author: Johann Dolivet

Exhaustivité (check and guess)
Ce script utilise une boucle while
Permet de calculer la racine cubique d'un cube parfait
"""

x = int(input("Entrez un nombre entier : "))
ans = 0
while ans ** 3 < abs(x):
    ans = ans + 1
if ans ** 3 != abs(x):
    print(x,"n'est pas un cube parfait")
else:
    if x < 0:
        ans = - ans
    print("La racine cubique de", x, "est", ans)
