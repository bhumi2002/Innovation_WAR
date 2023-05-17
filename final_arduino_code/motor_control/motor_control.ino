
#include <ros.h>
#include <std_msgs/Int32MultiArray.h>
ros::NodeHandle motor;

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
//--------------------------4 wheel 
#define left_dir1  13
#define left_dir2  16
#define right_dir1 15
#define right_dir2  14

#define left_pwm1  12
#define left_pwm2  9
#define right_pwm1 7
#define right_pwm2  5

std_msgs::Int32MultiArray pwm;
std_msgs::Int32MultiArray m;

//drawer0 , drawer1, drawer2, drawer3, shield, fire extinguisher servo, fire extinguisher normal, robotic arm stepper1+linear actuator(up down) , robotic arm stepper2(left right), gripper
int motor_direction[10]={2,42,48,52,17,-1 ,51 ,39 ,25,38};
int motor_pwm[10]={4,8,10,11,3,44,45 ,46,27,6}; //motor_pwm[5]=servo_pwm_pin

//servo motor
#define stepper_1_enable 58
#define stepper_1_direction 59
#define stepper_1_pulse 60

#define stepper_2_enable 23
#define stepper_2_direction 25
#define stepper_2_pulse 27

void module(const std_msgs::Int32MultiArray& m){
  if(m.data[0]==5){
    if(m.data[1]==1){
        for (pos = 0; pos <= 20; pos += 1) { // goes from 0 degrees to 180 degrees
          // in steps of 1 degree
          myservo.write(pos);              // tell servo to go to position in variable 'pos'
          delay(15);                       // waits 15ms for the servo to reach the position
        }
    }else if(m.data[1]==0){
        for (pos = 20; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
          myservo.write(pos);              // tell servo to go to position in variable 'pos'
          delay(15);                       // waits 15ms for the servo to reach the position
        } 
      }  
  }else if (m.data[0]==7){
      if(m.data[1]==1){
        digitalWrite(motor_direction[m.data[0]],HIGH);
          digitalWrite ( stepper_1_enable, LOW );
          delay ( 1 );
          digitalWrite ( stepper_1_direction, HIGH );
          delay ( 1 );
          digitalWrite ( stepper_1_pulse, LOW );
          delay ( 1 );
          digitalWrite ( stepper_1_pulse, HIGH );
          delay ( 1 );        
      }else if(m.data[1]==0){
        digitalWrite(motor_direction[m.data[0]],LOW);
          digitalWrite ( stepper_1_enable, LOW );
          delay ( 1 ); 
          digitalWrite ( stepper_1_direction, LOW );
          delay ( 1 );
          digitalWrite ( stepper_1_pulse, LOW );
          delay ( 1 );
          digitalWrite ( stepper_1_pulse, HIGH );
          delay ( 1 );   
      }
      analogWrite(motor_pwm[m.data[0]],m.data[2]);    
  }else if(m.data[0]==8){
      if(m.data[1]==1){
          digitalWrite ( stepper_2_enable, LOW );
          delay ( 1 ); 
          digitalWrite ( stepper_2_direction, HIGH );
          delay ( 1 );
          digitalWrite ( stepper_2_pulse, LOW );
          delay ( 1 );
          digitalWrite ( stepper_2_pulse, HIGH );
          delay ( 1 );
      }else if(m.data[1]==0){
          digitalWrite ( stepper_2_enable, LOW );
          delay ( 1 ); 
          digitalWrite ( stepper_2_direction, LOW );
          delay ( 1 );
          digitalWrite ( stepper_2_pulse, LOW );
          delay ( 1 );
          digitalWrite ( stepper_2_pulse, HIGH );
          delay ( 1 );    
      }    
  }else{
      if(m.data[1]==1){
        digitalWrite(motor_direction[m.data[0]],HIGH);
      }else if(m.data[1]==0){
        digitalWrite(motor_direction[m.data[0]],LOW);    
      }
      analogWrite(motor_pwm[m.data[0]],m.data[2]);
  } 
}

void motor_control(const std_msgs::Int32MultiArray& pwm )
{
  if(pwm.data[0]>255){
    digitalWrite(left_dir1,HIGH);
    analogWrite(left_pwm1,int((pwm.data[0]-255)/2));  
    digitalWrite(left_dir2,HIGH);
    analogWrite(left_pwm2,int((pwm.data[0]-255)/2));
  }else{
    digitalWrite(left_dir1,LOW);
    analogWrite(left_pwm1,int((255-pwm.data[0])/2));  
    digitalWrite(left_dir2,LOW);
    analogWrite(left_pwm2,int((255-pwm.data[0])/2));
  }
  if(pwm.data[1]>255){
    digitalWrite(right_dir1,HIGH);
    analogWrite(right_pwm1,int((pwm.data[1]-255)/2));  
    digitalWrite(right_dir2,HIGH);
    analogWrite(right_pwm2,int((pwm.data[1]-255)/2));
  }else{
    digitalWrite(right_dir1,LOW);
    analogWrite(right_pwm1,int((255-pwm.data[1])/2));  
    digitalWrite(right_dir2,LOW);
    analogWrite(right_pwm2,int((255-pwm.data[1])/2));
  } 
}

ros::Subscriber<std_msgs::Int32MultiArray> pwm_sub("pwm", &motor_control );
ros::Subscriber<std_msgs::Int32MultiArray> module_sub("Don", &module );

void setup()
{ 
  Serial.begin(57600);
  pinMode(left_dir1, OUTPUT);
  pinMode(left_dir2, OUTPUT);
  pinMode(right_dir1, OUTPUT);
  pinMode(right_dir2, OUTPUT);
  pinMode(left_pwm1, OUTPUT);
  pinMode(left_pwm2, OUTPUT);
  pinMode(right_pwm1, OUTPUT);
  pinMode(right_pwm2, OUTPUT);
  
  pinMode(motor_direction[0], OUTPUT);
  pinMode(motor_direction[1], OUTPUT);
  pinMode(motor_direction[2], OUTPUT);
  pinMode(motor_direction[3], OUTPUT);
  pinMode(motor_direction[4], OUTPUT);
//  pinMode(motor_direction[5], OUTPUT);
  pinMode(motor_direction[6], OUTPUT);
  pinMode(motor_direction[7], OUTPUT);
  pinMode(motor_direction[8], OUTPUT);
  pinMode(motor_direction[9], OUTPUT);
  myservo.attach(motor_pwm[5]);   
  pinMode(motor_pwm[0], OUTPUT);
  pinMode(motor_pwm[1], OUTPUT);
  pinMode(motor_pwm[2], OUTPUT);
  pinMode(motor_pwm[3], OUTPUT);
  pinMode(motor_pwm[4], OUTPUT);
//  pinMode(motor_pwm[5], OUTPUT);
  pinMode(motor_pwm[6], OUTPUT);
  pinMode(motor_pwm[7], OUTPUT);
  pinMode(motor_pwm[8], OUTPUT);
  pinMode(motor_pwm[9], OUTPUT);

  pinMode(stepper_1_enable, OUTPUT);
  pinMode(stepper_1_pulse, OUTPUT);
  motor.getHardware()->setBaud(57600);
  motor.initNode();
  motor.subscribe(pwm_sub);
  motor.subscribe(module_sub);
}

void loop()
{  
  motor.spinOnce();
  delay(1);
}
