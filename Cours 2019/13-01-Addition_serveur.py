"""
Created on 08-21-2019

@author: Johann Dolivet

Communication client - serveur
Utilisation du module socket
Programme serveur : ajoute les 2 nombres envoyés par le client
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*

# Définition d'un serveur réseau rudimentaire
# Ce serveur attend la connexion d'un client
# La connexion est interrompue lorsque le client entre une valeur non entière

import socket, sys

HOST = ""  # IP du serveur
PORT = 50000


# 1) création du socket :
connexionPrincipale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) liaison du socket à une adresse précise :
try:
    connexionPrincipale.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")    
    sys.exit()
 
# 3) Attente de la requête de connexion d'un client :    
print("Serveur prêt, en attente de requêtes ...")    
connexionPrincipale.listen(2)
 
# 4) Etablissement de la connexion :    
connexionClient, adresse = connexionPrincipale.accept()      
print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))

# 5) Dialogue avec le client :    
msgServeur ="Vous êtes connecté au serveur. Entrez vos nombres entiers."    
connexionClient.send(msgServeur.encode())    
msgClient1 = connexionClient.recv(1024).decode()
msgClient2 = connexionClient.recv(1024).decode()
while True:  
    if msgClient1.upper() == "FIN" or msgClient2.upper() == "FIN":
        break      
    print("A = ", msgClient1)
    print("B = ", msgClient2)
    msgServeur=str(int(msgClient1)+int(msgClient2))
    connexionClient.send(msgServeur.encode())
    msgClient1 = connexionClient.recv(1024).decode()
    msgClient2 = connexionClient.recv(1024).decode() 


# 6) Fermeture de la connexion :    
connexionClient.send("fin".encode())    
print("Connexion interrompue.")    
connexionClient.close()
connexionPrincipale.close()
