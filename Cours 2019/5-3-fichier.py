"""
Created on 03-20-2019

@author: Johann Dolivet

Manipulation de fichier : écriture
Ce programme permet d'écrire dans un fichier
"""

fichierManip = open("eleves.txt", 'w')  # Si le fichier n'existe pas, il sera créé

for i in range(2):
    nom = input("Entrez votre nom : ")
    fichierManip.write(nom + '\n')  # retour ligne après chaque entrée

fichierManip.close()                    # Ne pas oublier de fermer!
