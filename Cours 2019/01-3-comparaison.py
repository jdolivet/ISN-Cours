# -*- coding: utf-8 -*-
"""
Created on 02-06-2019

@author: Johann Dolivet

Instruction conditionnelle et expression booléenne composée
Ce script permet de déterminer le plus petit nombre parmi x, y ou z
"""

x = 12
y = 13
z = 15
 
if x < y and x < z:
    print("x est le plus petit")
elif y < z:
    print("y est le plus petit")
else:
    print("z est le plus petit")
