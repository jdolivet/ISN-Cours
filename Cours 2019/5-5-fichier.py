"""
Created on 03-20-2019

@author: Johann Dolivet

Manipulation de fichier : ajouter
Ce programme permet d'ajouter du contenu dans un fichier
"""

fichierManip = open("eleves.txt", 'a')

name = input("Entrez votre nom : ")
fichierManip.write(name + '\n')

fichierManip.close()    # Ne pas oublier de fermer!
                   


