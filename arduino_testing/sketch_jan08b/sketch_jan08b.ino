
#include <Servo.h>

Servo myservo; //create servo object

int val;
String inString = ""; //string to hold input

void setup() {
  Serial.begin(9600);
   // put your setup code here, to run once:
  myservo.attach(22);
  myservo.write(0);

  while (!Serial);
  
 
}

void loop() {
  // put your main code here, to run repeatedly:
  
  while (val < 180) {
    myservo.write(val);
    val += 10;
    delay(1000);
  }
  
  
  
  }
