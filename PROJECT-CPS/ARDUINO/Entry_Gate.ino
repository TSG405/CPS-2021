#include <Servo.h> 
#define echoPin 4 // Connecting pin D4 Arduino to pin Echo of HC-SR04
#define trigPin 5 // Connecting pin D5 Arduino to pin Trig of HC-SR04

int servoPin = 6; 
Servo Servo1; 

long duration; // sound wave travel time
int distance; // Distance measurement
bool isOpen=false;
int ledPin=11;


void setup() { 
  Servo1.attach(servoPin); 
  pinMode(trigPin, OUTPUT); 
  pinMode(echoPin, INPUT); 
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); 
  Servo1.write(95);
}


void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
 
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trigPin, LOW);
 
  duration = pulseIn(echoPin, HIGH);
 
  distance = duration * 0.034 / 2; 
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  if(distance < 20)
  {
    digitalWrite(ledPin, HIGH);
    // call -- Main.py()
    opengate();
  }
  else
  {
    closeGate();
    digitalWrite(ledPin, LOW);
  }
  
delay(5000);
}


void closeGate()
{
   if(isOpen) {
   Servo1.write(0); 
   isOpen=false;
 }
}


void opengate()
{ 
  if(!isOpen) 
  {
    Servo1.write(95); 
  }
   isOpen=true;
   delay(2000);   
}


'''
@ ~ TSG405,2021
'''
