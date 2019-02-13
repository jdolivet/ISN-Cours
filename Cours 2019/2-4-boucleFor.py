"""
Created on 02-13-2019

@author: Johann Dolivet

Instruction iterative
Ce script montre quelques exemples élémentaires d'utilisation de boucles for
"""

# Utilisation de la fonction range()
x = 4
for i in range(0, x):
    print(i)

print("--------")

# La fonction range() est évaluée avant l'exécution de la boucle
x = 4
for i in range(x):
    print(i)
    x = 5

print("--------")

# Boucles imbriquées
x = 4
for i in range(x):
    for j in range(x):
        print(j)

print("--------")

# Modification de la variable en cours d'execution
x = 4
for i in range(x):
    for j in range(x):
        print(j)
        x = 2
