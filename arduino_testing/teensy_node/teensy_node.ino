

#include <ros.h>

/*
#if defined(ARDUINO) && ARDUINO >= 100
  #include "Arduino.h"
#else
  #include <WProgram.h>
#endif
*/

#include <Servo.h>
#include <geometry_msgs/Vector3.h>
#include <std_msgs/UInt16.h>

Servo myservo; //create servo object

ros::NodeHandle  nh;
String inString = "";


void servo_cb( const geometry_msgs::Vector3& cmd_msg){
  myservo.write(cmd_msg.x);
  /*inString = cmd_msg.x;
  myservo.write(90);
  delay(10);
  myservo.write(inString.toInt());//set servo angle, should be from 0-180  
  */
}


/*
void servo_cb( const std_msgs::UInt16& cmd_msg){
  myservo.write(cmd_msg.data);
  
}
*/


ros::Subscriber<geometry_msgs::Vector3> sub("gimbal_control", servo_cb);

//ros::Subscriber<std_msgs::UInt16> sub("gimbal_control", servo_cb);

void setup(){
  pinMode(22, OUTPUT);

  nh.initNode();
  nh.subscribe(sub);
  
  myservo.attach(22); //attach it to pin 9
  myservo.write(0);
}

void loop(){
  nh.spinOnce();
  delay(1);
}
