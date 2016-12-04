int option;
// suponemos conectado el led al pin 13
int led = 13;
void setup(){
    Serial.begin(9600);
    pinMode(led, OUTPUT);
}

void loop(){
  //si existe datos disponibles los leemos
  if (Serial.available()>0){
    //leemos la opcion enviada
    option=Serial.read();
    if(option=='a') {
        Serial.println("ON");
        digitalWrite(led, HIGH);
        delay(3000);  
    }
    if(option=='b') {
        Serial.println("OFF");
        digitalWrite(led, LOW);

    }
    if (option=='c') {
        Serial.println("Flashing LED"); 
        digitalWrite(led, HIGH); 
        delay(1000);             
        digitalWrite(led, LOW);    
        delay(500); 
        digitalWrite(led, HIGH); 
        delay(1000);         
        digitalWrite(led, LOW);  
   
                    }
  }
}

  
