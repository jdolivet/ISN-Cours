# -*- coding: utf-8 -*-
"""
Created on 02-10-2020

@author: Johann Dolivet

Instructions conditionnelles imbriquées
Ce script permet de déterminer si le nombre x est divisible par 2 et/ou par 3
"""

x = 1234567754

if x % 2 == 0:
    if x % 3 == 0:
        print("divisible par 2 et par 3")
    else:
        print("divisible par 2 mais pas par 3")
elif x % 3 == 0:
    print("divisible par 3 mais pas par 2")
else:
    print("divisible ni par 2 ni par 3")
