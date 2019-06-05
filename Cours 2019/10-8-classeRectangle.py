"""
Created on 06-05-2019

@author: Johann Dolivet

Programmation Orientée Objet
Illustration du concept de polymorphisme
Redéfinition de la fonction print()
"""

class Rectangle:
    """Classe Rectangle.
    Attributs : hauteur et largeur
    Méthodes : surface() et perimetre()"""
    
    def __init__(self, hauteur, largeur):
        """Constructeur de la classe"""
        self.hauteur = hauteur
        self.largeur = largeur

    def __str__(self):
        """Paramètrage de la fonction print() sur cette classe"""
        return "<"+str(self.hauteur)+", "+str(self.largeur)+">"

    def surface(self):
        """Méthode retournant la surface du rectangle considéré"""
        return self.hauteur * self.largeur
    
    def perimetre(self):
        """Méthode retournant le périmètre du rectangle considéré"""
        return 2 * (self.largeur + self.hauteur)


class Carre(Rectangle):
    """Classe Carre.
    Hérite de la classe Rectangle
    Attribut : cote"""
    
    def __init__(self, cote):
        """Constructeur de la classe"""
        Rectangle.__init__(self, cote, cote)
        self.cote = cote
