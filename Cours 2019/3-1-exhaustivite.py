"""
Created on 02-20-2019

@author: Johann Dolivet

Exhaustivité (check and guess)

Ce script utilise une boucle for

Permet de calculer la racine cubique d'un cube parfait
"""

x = int(input("Entrez un nombre entier : "))
for ans in range(abs(x) + 1):
   if ans ** 3 >= abs(x):
       break    # L'instruction break permet de sortir de la boucle
if ans ** 3 != abs(x):
    print(x,"n'est pas un cube parfait")
else:
    if x < 0:
        ans = - ans
    print("La racine cubique de", x, "est", ans)
