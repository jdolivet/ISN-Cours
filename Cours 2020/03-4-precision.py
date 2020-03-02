"""
Created on 03-02-2020

@author: Johann Dolivet

Précision des calculs sur les flottants

Certains modules permettent de nous aider à gérer les problèmes de précisions
"""


from decimal import Decimal

x = Decimal('0.0')
nbIter = 3
for i in range(nbIter):
    x = x + Decimal('0.1')
print(nbIter, "* 0.1 =", x)
