"""
Created on 06-05-2019

@author: Johann Dolivet

Programmation Orientée Objet
Illustration du concept d'encapsulation et d'abstraction
Définition des attributs et des méthodes de la classe
"""

class Rectangle:
    """Classe Rectangle.
    Attributs : hauteur et largeur
    Méthodes : surface() et perimetre()"""
    
    def __init__(self, hauteur, largeur):
        """Constructeur de la classe"""
        self.hauteur = hauteur
        self.largeur = largeur

    def surface(self):
        """Méthode retournant la surface du rectangle considéré"""
        return self.hauteur * self.largeur
    
    def perimetre(self):
        """Méthode retournant le périmètre du rectangle considéré"""
        return 2 * (self.largeur + self.hauteur)

