/*
 * rosserial PubSub Example
 * Prints "hello world!" and toggles led
 */

#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <HCSR04.h>
ros::NodeHandle  nh;

HCSR04 hc1(13, 12); //initialisation class HCSR04 (trig pin , echo pin)
HCSR04 hc2(11, 10); //initialisation class HCSR04 (trig pin , echo pin)
HCSR04 hc3(9, 8);   //initialisation class HCSR04   (trig pin , echo pin)
HCSR04 hc4(7, 6);   //initialisation class HCSR04   (trig pin , echo pin)
HCSR04 hc5(2, 4);   //initialisation class HCSR04   (trig pin , echo pin)

std_msgs::Float32MultiArray str_msg;
ros::Publisher chatter("chatter", &str_msg);

void setup()
{
  Serial.begin(57600);
  nh.getHardware()->setBaud(57600);
  nh.initNode();
  str_msg.data_length = 5;
  str_msg.data = (float *)malloc((sizeof(float))*str_msg.data_length * 2);
  nh.advertise(chatter);
}

void loop()
{
  str_msg.data[0] = hc1.dist();
  str_msg.data[1] = hc2.dist();
  str_msg.data[2] = hc3.dist();
  str_msg.data[3] = hc4.dist();
  str_msg.data[4] = hc5.dist();
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(150);
}
