"""
Created on 08-21-2019

@author: Johann Dolivet

Communication client - serveur
Utilisation du module socket
Programme client : envoie 2 nombres au serveur
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*

# Définition d'un client réseau rudimentaire
# Ce client dialogue avec un serveur ad hoc
# La connexion est interrompue lorsque le client entre une valeur non entière

import socket, sys

HOST = ""   # A RENSEIGNER : IP du serveur 
PORT = 50000

# 1) création du socket :
connexionServeur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) envoi d'une requête de connexion au serveur :
try:    
    connexionServeur.connect((HOST, PORT))
except socket.error:    
    print("La connexion a échouée.")    
    sys.exit()
print("Connexion établie avec le serveur.")

# 3) Dialogue avec le serveur :
msgServeur = connexionServeur.recv(1024).decode()
print(msgServeur)
while True:    
    msgClient1 = input("A = ")
    if msgClient1.isnumeric():
        connexionServeur.send(msgClient1.encode())
    else:
        connexionServeur.send("fin".encode())
    msgClient2 = input("B = ")
    if msgClient2.isnumeric():
        connexionServeur.send(msgClient2.encode())
    else:
        connexionServeur.send("fin".encode())
    msgServeur = connexionServeur.recv(1024).decode()
    if msgServeur.upper() == "FIN":
        break
    print("A + B = ", msgServeur)
 
# 4) Fermeture de la connexion :
connexionServeur.send("fin".encode())
print("Connexion interrompue.")
connexionServeur.close()
