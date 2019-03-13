"""
Created on 03-13-2019

@author: Johann Dolivet

Précision des calculs sur les flottants

Attention à la manipulation des nombres décimaux
"""


x = 0.0
nbIter = 3
for i in range(nbIter):
    x = x + 0.1
print(nbIter, "* 0.1 =", x)
