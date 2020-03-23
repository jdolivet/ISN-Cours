"""
Created on 03-23-2020

@author: Johann Dolivet

Marche aléatoire
Ce programme nécessite l'import de modules built-in
"""

from turtle import *
from random import randint

for i in range(500):
    k = randint(0, 3)
    left(k * 90)
    forward(10)
