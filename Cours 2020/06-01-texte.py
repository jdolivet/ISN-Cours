"""
Created on 04-13-2020

@author: Johann Dolivet

Représentation des caractères
Ce programme permet de récupérer un fichier texte en ligne.
Le fichier est transmis puis décodé octet par octet.
(norme UTF-8)
"""

from urllib.request import urlopen 

connection = urlopen('https://sites.google.com/site/\
sciencesdunumerique/information/Textes/Zen.txt') 
zen = connection.read()
connection.close()
for octet in zen:
    symbole = chr(octet)
    print(symbole, end='')


####Texte original :
##The Zen of Python, by Tim Peters
##
##Beautiful is better than ugly.
##Explicit is better than implicit.
##Simple is better than complex.
##Complex is better than complicated.
##Flat is better than nested.
##Sparse is better than dense.
##Readability counts.
##Special cases aren't special enough to break the rules.
##Although practicality beats purity.
##Errors should never pass silently.
##Unless explicitly silenced.
##In the face of ambiguity, refuse the temptation to guess.
##There should be one-- and preferably only one --obvious way to do it.
##Although that way may not be obvious at first unless you're Dutch.
##Now is better than never.
##Although never is often better than *right* now.
##If the implementation is hard to explain, it's a bad idea.
##If the implementation is easy to explain, it may be a good idea.
##Namespaces are one honking great idea -- let's do more of those!
