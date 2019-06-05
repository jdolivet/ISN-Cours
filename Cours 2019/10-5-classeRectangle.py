"""
Created on 06-05-2019

@author: Johann Dolivet

Programmation Orientée Objet
Illustration du concept d'encapsulation et d'abstraction
Définition des attributs de la classe
"""

class Rectangle:
    """Classe Rectangle.
    Attributs : hauteur et largeur"""
    
    def __init__(self, hauteur, largeur):
        """Constructeur de la classe"""
        self.hauteur = hauteur
        self.largeur = largeur

