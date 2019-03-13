"""
Created on 03-13-2019

@author: Johann Dolivet

Fonctions

Utilisation des paramètres
"""

def affiche_nom(prenom, nom, reverse = False):
    if reverse:
        print(nom, ',', prenom)
    else:
        print(prenom, ',', nom)

affiche_nom("Alan", "Turing")
affiche_nom("Alan", "Turing", True)
affiche_nom(nom = "Turing", prenom = "Alan", reverse = True)
