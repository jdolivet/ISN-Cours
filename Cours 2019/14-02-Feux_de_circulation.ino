/*
Fonctionnement :
  Feu voiture
    - Orange allumée pendant 1 seconde
    - Rouge allumée pendant 3 secondes
    - Verte allumée pendant 3 secondes
  Feu Piéton : 
    - Rouge si Feu voiture vert ou orange
    - Vert si Feu voiture rouge
*/


// Initialisation des constantes :
const int ledVoitureOrange = 11;	// Numéro de la broche à laquelle est connectée la LED Orange du Feu Voiture
const int ledVoitureRouge = 12;		// Numéro de la broche à laquelle est connectée la LED Rouge du Feu Voiture
const int ledVoitureVerte = 10;		// Numéro de la broche à laquelle est connectée la LED Verte du Feu Voiture
const int ledPietonRouge = 9;		// Numéro de la broche à laquelle est connectée la LED Rouge du Feu Pieton
const int ledPietonVerte = 8;		// Numéro de la broche à laquelle est connectée la LED Verte du Feu Pieton

// Déclaration des variables :
int buttonState = 0;         // variable qui sera utilisée pour stocker l'état du bouton 

// le code dans cette fonction est exécuté une fois au début
void setup() {
  // indique que les broches de LED sont des sortie :
  pinMode(ledVoitureOrange, OUTPUT);
  pinMode(ledVoitureRouge, OUTPUT);
  pinMode(ledVoitureVerte, OUTPUT);
  pinMode(ledPietonRouge, OUTPUT);
  pinMode(ledPietonVerte, OUTPUT);
}
 
// le code dans cette fonction est exécuté en boucle
void loop() { 
 
  digitalWrite(ledPietonVerte, LOW);    	// éteindre la LED Pieton Vert
  digitalWrite(ledPietonRouge, HIGH);   	// allumer la LED Pieton Rouge
  digitalWrite(ledVoitureRouge, LOW);   	// éteindre la LED Voiture Rouge 
  digitalWrite(ledVoitureVerte, HIGH);   	// allumer la LED Voiture Vert 
  delay(3000);   	
    
  digitalWrite(ledVoitureVerte, LOW);    	// éteindre la LED Voiture Verte
  digitalWrite(ledVoitureOrange, HIGH);   	// allumer la LED Voiture Orange
  delay(1000);               				// attendre 1s
  
  digitalWrite(ledVoitureOrange, LOW);    	// éteindre la LED Voiture Orange
  digitalWrite(ledVoitureRouge, HIGH);   	// allumer la LED Voiture Rouge
  digitalWrite(ledPietonRouge, LOW);   		// éteindre la LED Pieton Rouge 
  digitalWrite(ledPietonVerte, HIGH);   	// allumer la LED Pieton Vert 
  delay(3000);
  
}