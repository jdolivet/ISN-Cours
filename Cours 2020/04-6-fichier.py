"""
Created on 03-23-2020

@author: Johann Dolivet

Manipulation de fichier : lecture
Ce programme permet de lire le contenu d'un fichier
Le fichier dot être dans le répertoire courant 
"""

fichierManip = open("eleves.txt", 'r')  # Le fichier doit exister!

for line in fichierManip:
    print(line[:-1])                    # On ne souhaite pas imprimer le dernier caractère
    
fichierManip.close()                    # Ne pas oublier de fermer!


