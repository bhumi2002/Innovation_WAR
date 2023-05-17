/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <geometry_msgs/Twist.h>
ros::NodeHandle  nh;

//--------------------------4 wheel 
#define left_dir1  2
//#define left_dir2  16
#define right_dir1 11
//#define right_dir2  14

#define left_pwm1  3
//#define left_pwm2  9
#define right_pwm1 10
//#define right_pwm2  5

float left=0,right=0;
int PWM1=0,PWM2=0;

//geometry_msgs::Twist str_msg;
geometry_msgs::Twist toggle_msg;
//ros::Publisher chatter("chatter", &str_msg);

void messageCb(const geometry_msgs::Twist &toggle_msg )
{
    left=toggle_msg.linear.x+toggle_msg.angular.z;
    right=toggle_msg.linear.x-toggle_msg.angular.z;
    PWM1=(left+1)*510/2;
    PWM2=(right+1)*510/2;
    //str_msg=toggle_msg;
    //chatter.publish(&str_msg);
    if(PWM1>255){
      digitalWrite(left_dir1,HIGH);
      analogWrite(left_pwm1,int((PWM1-255)/2)); 
//      digitalWrite(left_dir2,HIGH);
//      analogWrite(left_pwm2,int((PWM1-255)/2)); 
    }else{
      digitalWrite(left_dir1,LOW);
      analogWrite(left_pwm1,int((255-PWM1)/2));
//      digitalWrite(left_dir2,LOW);
//      analogWrite(left_pwm2,int((255-PWM1)/2));
    }
    if(PWM2>255){
      digitalWrite(right_dir1,HIGH);
      analogWrite(right_pwm1,int((PWM2-255)/2));
//      digitalWrite(right_dir2,HIGH);
//      analogWrite(right_pwm2,int((PWM2-255)/2));
    }else{
      digitalWrite(right_dir1,LOW);
      analogWrite(right_pwm1,int((255-PWM2)/2));
//      digitalWrite(right_dir2,LOW);
//      analogWrite(right_pwm2,int((255-PWM2)/2));
    } 
}

ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", &messageCb );

void setup()
{ 
  Serial.begin(115200);
  pinMode(left_dir1, OUTPUT);
//  pinMode(left_dir2, OUTPUT);
  pinMode(right_dir1, OUTPUT);
//  pinMode(right_dir2, OUTPUT);
  pinMode(left_pwm1, OUTPUT);
//  pinMode(left_pwm2, OUTPUT);
  pinMode(right_pwm1, OUTPUT);
//  pinMode(right_pwm2, OUTPUT);
  nh.getHardware()->setBaud(115200);
  nh.initNode();
//  nh.advertise(chatter);
  nh.subscribe(sub);
}

void loop()
{  
//  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(1);
}
