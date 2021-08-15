#include <Servo.h>
int Red = 7;
int Blue = 5;
int Green = 2;
int pinPot = A1;
int potValue = 0;
int val;
Servo servo1;
 
void setup() {
servo1.attach(9); 
Serial.begin(9600);  
  pinMode(Red, OUTPUT);
  pinMode(Blue, OUTPUT);
  pinMode(Green, OUTPUT); 
}
 
void loop() {
  val = analogRead(potValue);
  val = map(val, 0, 1023, 0, 180); 
  servo1.write(val);
    
  if(val<=60){
    digitalWrite(Red, HIGH);
    delay(1000);
    digitalWrite(Red, LOW);
    delay(1000);
  }
  
  if(val<=120){
    digitalWrite(Blue, HIGH);
    delay(1000);
    digitalWrite(Blue, LOW);
    delay(1000);
  }
 
  if(val<=180){
    digitalWrite(Green, HIGH);
    delay(1000);
    digitalWrite(Green, LOW);
    delay(1000);
  }
}

