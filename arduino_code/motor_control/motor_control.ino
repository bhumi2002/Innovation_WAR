
#include <ros.h>
#include <std_msgs/Int32MultiArray.h>
ros::NodeHandle motor;

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

//drawer0, drawer1, drawer2, drawer3, fire extinguisher, robotic arm stepper1, stepper2, stepper3, shield motor, servo motor [10]
int motor_direction[10]={2,8,10,11,17,-1 ,-1 ,-1 ,51,-1};
int motor_pwm[10]={4,42,48,52,3,-1 ,-1 ,-1 ,45,-1}; //motor_pwm[9]=servo_pwm_pin

//servo motor
#define servo_vcc_pin -1
#define servo_gnd_pin -1

void module(const std_msgs::Int32MultiArray& m){
  if(m.data[0]==9){
    if(m.data[1]==1){
        digitalWrite(servo_vcc_pin,HIGH);
        digitalWrite(servo_vcc_pin,LOW);
    }else if(m.data[1]==0){
        digitalWrite(servo_vcc_pin,LOW);
        digitalWrite(servo_vcc_pin,HIGH); 
      }  
  }else{
      if(m.data[1]==1){
        digitalWrite(motor_direction[m.data[0]],HIGH);
      }else if(m.data[1]==0){
        digitalWrite(motor_direction[m.data[0]],LOW);    
      }
    }
  analogWrite(motor_pwm[m.data[0]],m.data[2]); 
}

void motor_control(const std_msgs::Int32MultiArray& pwm )
{
  if(pwm.data[0]>255){
    digitalWrite(left_dir1,HIGH);
    analogWrite(left_pwm1,(pwm.data[0]-255));  
    digitalWrite(left_dir2,HIGH);
    analogWrite(left_pwm2,(pwm.data[0]-255));
  }else{
    digitalWrite(left_dir1,LOW);
    analogWrite(left_pwm1,(pwm.data[0]));  
    digitalWrite(left_dir2,LOW);
    analogWrite(left_pwm2,(pwm.data[0]));
  }
  if(pwm.data[1]>255){
    digitalWrite(right_dir1,HIGH);
    analogWrite(right_pwm1,(pwm.data[1]-255));  
    digitalWrite(right_dir2,HIGH);
    analogWrite(right_pwm2,(pwm.data[1]-255));
  }else{
    digitalWrite(right_dir1,LOW);
    analogWrite(right_pwm1,(pwm.data[1]));  
    digitalWrite(right_dir2,LOW);
    analogWrite(right_pwm2,(pwm.data[1]));
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
  pinMode(motor_direction[5], OUTPUT);
  pinMode(motor_direction[6], OUTPUT);
  pinMode(motor_direction[7], OUTPUT);
  pinMode(motor_direction[8], OUTPUT);
  
  pinMode(motor_pwm[0], OUTPUT);
  pinMode(motor_pwm[1], OUTPUT);
  pinMode(motor_pwm[2], OUTPUT);
  pinMode(motor_pwm[3], OUTPUT);
  pinMode(motor_pwm[4], OUTPUT);
  pinMode(motor_pwm[5], OUTPUT);
  pinMode(motor_pwm[6], OUTPUT);
  pinMode(motor_pwm[7], OUTPUT);
  pinMode(motor_pwm[8], OUTPUT);
  
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
