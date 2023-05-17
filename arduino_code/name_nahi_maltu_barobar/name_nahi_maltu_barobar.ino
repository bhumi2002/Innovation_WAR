
#include <HCSR04.h>

#define left_dir A0
#define left_pwm 5
#define right_dir A1
#define right_pwm 3
#include <ros.h>
#include <geometry_msgs/Twist.h>
ros::NodeHandle  nh;


geometry_msgs::Twist str_msg;
ros::Publisher chatter("chatter", &str_msg);
HCSR04 hc1(13, 12); //initialisation class HCSR04 (trig pin , echo pin)
HCSR04 hc2(11, 10); //initialisation class HCSR04 (trig pin , echo pin)
HCSR04 hc3(9, 8);   //initialisation class HCSR04   (trig pin , echo pin)
HCSR04 hc4(7, 6);   //initialisation class HCSR04   (trig pin , echo pin)
HCSR04 hc5(2, 4);   //initialisation class HCSR04   (trig pin , echo pin)
float distance[5],angular=0,linear=0,left=0,right=0,temp=0;
int PWM1=0,PWM2=0;

void setup()
{
  Serial.begin(9600);
  pinMode(left_dir, OUTPUT);
  pinMode(left_pwm, OUTPUT);
  pinMode(right_dir, OUTPUT);
  pinMode(right_pwm, OUTPUT);
  nh.getHardware()->setBaud(9600);
  nh.initNode();
  nh.advertise(chatter);
}

void loop()
{
     distance[4]=hc1.dist();
     distance[3]=hc2.dist();
     distance[2]=hc3.dist();
     distance[1]=hc4.dist();
     distance[0]=hc5.dist();
     for(int i=0;i<5;i++){
        if(distance[i]>120 || distance[i]==0){
              distance[i]=120;
        } 
     }
    temp=(2*distance[3])+distance[4]-(2*distance[1])-distance[0]; 
    temp=temp/(distance[0]+distance[1]+distance[3]+distance[4]+distance[2]); 
    linear=1.2*(1-abs(temp));
    angular=temp*1.2;
    if(distance[2]<50){
            linear=-1;
            angular=1.5;
    }
    left=linear+(angular);
    right=linear-(angular);
    PWM1 = int(((left+1)/3)*510);
    PWM2 = int(((right+1)/3)*510);
    str_msg.linear.x=linear;
    str_msg.angular.z=angular;
    chatter.publish( &str_msg );
    Serial.print(left);
    Serial.print("                ");
    Serial.println(right);
    if(PWM1>255){
            digitalWrite(left_dir,LOW);
            analogWrite(left_pwm,(PWM1-255));  
    }else{
            digitalWrite(left_dir,HIGH);
            analogWrite(left_pwm,(255-PWM1));
    }
    if(PWM2>255){
            digitalWrite(right_dir,LOW);
            analogWrite(right_pwm,(PWM2-255));
    }else{
            digitalWrite(right_dir,HIGH);
            analogWrite(right_pwm,(255-PWM2));
    } 
    delay(10);                      // we suggest to use over 60ms measurement cycle, in order to prevent trigger signal to the echo signal.

}
