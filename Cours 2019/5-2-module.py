"""
Created on 03-20-2019

@author: Johann Dolivet

Marche aléatoire
Ce programme précise de l'import de modules built-in
"""

from turtle import *
from random import randint

for i in range(500):
    k = randint(0, 3)
    left(k * 90)
    forward(10)
