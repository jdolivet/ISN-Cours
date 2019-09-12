/*
Feu tricolore
- Orange allumée pendant 1 seconde
- Rouge allumée pendant 3 secondes
- Verte allumée pendant 3 secondes
*/


// Numéro des broche auxquelles sont
// connectées les LED
int ledOrange = 13;
int ledRouge = 12;
int ledVerte = 11;
 
// le code dans cette fonction est exécuté une fois au début
void setup() {
  // indique que la broche de la LED une sortie :
  // on va modifier sa tension
  pinMode(ledOrange, OUTPUT);
  pinMode(ledRouge, OUTPUT);
  pinMode(ledVerte, OUTPUT);
}
 
// le code dans cette fonction est exécuté en boucle
void loop() {
  digitalWrite(ledOrange, HIGH);   	// allumer la LED Orange (tension 5V sur la broche)
  delay(1000);               		// attendre 1000ms = 1s
  digitalWrite(ledOrange, LOW);    	// éteindre la LED (tension 0V sur la broche)
    
  digitalWrite(ledRouge, HIGH);   	// allumer la LED Rouge(tension 5V sur la broche)
  delay(3000);               		// attendre 3000ms = 3s
  digitalWrite(ledRouge, LOW);    	// éteindre la LED (tension 0V sur la broche)
    
  digitalWrite(ledVerte, HIGH);   	// allumer la LED (tension 5V sur la broche)
  delay(3000);               		// attendre 3000ms = 3s
  digitalWrite(ledVerte, LOW);    	// éteindre la LED (tension 0V sur la broche)
}