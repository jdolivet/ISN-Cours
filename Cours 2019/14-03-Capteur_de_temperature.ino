/*
Capteur de temperature
On utilise un capteur TMP36 : 
La tension de sortie est proportionnelle à la température dans la plage de -40°C à +125°C.

On récupère une tension analogique, en entrée, à la porte A0
On convertit cette tension en temperature (selon le capteur)

Lorsque temperature <= 30 		: LED verte
Lorsque 30 < temperature <= 50 	: LED orange
Lorsque temperature > 50 		: LED rouge

On affiche des résultats via le moniteur série
*/


// Numéro des broche auxquelles sont
// connectées les LED
int ledOrange = 13;
int ledRouge = 12;
int ledVerte = 11;

int capteurTemp = A0;    // Port analogique pour lire la température

 
// le code dans cette fonction est exécuté une fois au début
void setup() {
  // indique que les broches des LED une sortie :
  // on va modifier sa tension
  pinMode(ledOrange, OUTPUT);
  pinMode(ledRouge, OUTPUT);
  pinMode(ledVerte, OUTPUT);
  // On établit la liaison série à 9600 bits par seconde
  Serial.begin(9600);
}
 
// le code dans cette fonction est exécuté en boucle
void loop() {
  // On lit la tension en A0
  int tension = analogRead(capteurTemp);
  
  // La tension est un entier qui va de 0 à 1024 fois la tension de 5V
  // On convertit en temperature en degré Celcius
  float temperature = (((tension * 5) / 1024.0) - 0.5) * 100;
  
  if (temperature > 50){
    digitalWrite(ledVerte, LOW);
    digitalWrite(ledOrange, LOW);
    digitalWrite(ledRouge, HIGH);
    Serial.print("Il fait trop chaud : ");
  }  
  else if (temperature <= 50 && temperature > 30){
    digitalWrite(ledVerte, LOW);
    digitalWrite(ledRouge, LOW);
    digitalWrite(ledOrange, HIGH);
    Serial.print("La temperature monte : ");
  }  
  else{
    digitalWrite(ledOrange, LOW);
    digitalWrite(ledRouge, LOW);
    digitalWrite(ledVerte, HIGH);
    Serial.print("La temperature reste agreable : ");
  }
  
  Serial.print(temperature);
  Serial.println(" degre Celsius");
  delay(1000);

}