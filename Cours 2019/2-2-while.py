"""
Created on 02-13-2019

@author: Johann Dolivet

Instruction iterative
Ce script utilise une boucle while
Permet de calculer le carré d'un nombre
"""

x = 3
ans = 0
iterStop = x
while (iterStop != 0):
    ans = ans + x
    iterStop = iterStop - 1
print(str(x) + ' * ' + str(x) + ' = ' + str(ans))
