"""
Created on 05-18-2020

@author: Johann Dolivet

Utilisation des dictionnaires
Les éléments ne sont pas identifiés par un indice (comme les tuples et listes).
Ils sont identifiés par une clé.
"""

dictionnaire = {}
dictionnaire['Louis'] = 'isn01'
dictionnaire['Victor'] = 2
dictionnaire['Louis'] = 3.0
dictionnaire['Matteo'] = ['Fernandez', 2020]
dictionnaire['Henri'] = ('Fernandez', 2020)

# On obtient :
# {'Louis': 3.0, 'Victor': 2, 'Matteo': ['Fernandez', 2020], 'Henri': ('Lima', 2020)}
