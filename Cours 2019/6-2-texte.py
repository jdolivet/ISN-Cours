"""
Created on 04-03-2019

@author: Johann Dolivet

Représentation des caractères
Ce programme permet de récupérer un fichier texte en ligne.
Le fichier est transmis puis décodé octet par octet.
Probleme d'affichage avec les caractères occupant plus d'un octet
(norme UTF-8)
"""

from urllib.request import urlopen

connection = urlopen('https://sites.google.com/site/\
sciencesdunumerique/information/Textes/Stroustrup.txt') 
zen = connection.read()
connection.close()
for octet in zen:
    symbole = chr(octet)
    print(symbole, end='') 


####Texte original :
##Der er en gammel historie om en person, som ønskede hans computer var lige så let at bruge som hans telefon. Dette ønske er gået i opfyldelse, da jeg ikke længere ved, hvordan man bruger min telefon.
##Bjarne Stroustrup
