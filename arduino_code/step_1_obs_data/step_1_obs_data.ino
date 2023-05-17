/*
 * rosserial PubSub Example
 * Prints "hello world!" and toggles led
 */

#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <HCSR04.h>
ros::NodeHandle sensor_data;

#define e1 10
#define t1 9
//#define e2 31
//#define t2 29
//#define e3 49
//#define t3 51
//#define e4 A13
//#define t4 A12
//#define e5 A9
//#define t5 A10

HCSR04 hc1(t1, e1);
//HCSR04 hc2(t2, e2); 
//HCSR04 hc3(t3, e3);   
//HCSR04 hc4(t4, e4);   
//HCSR04 hc5(t5, e5); 

std_msgs::Float32MultiArray obs_data;
ros::Publisher obs_publisher("obs_data", &obs_data);

void setup()
{
  Serial.begin(57600);
//  Wire.begin();
  sensor_data.initNode();
  sensor_data.getHardware()->setBaud(57600);
  obs_data.data_length = 1;
  obs_data.data = (float *)malloc((sizeof(float))*obs_data.data_length * 2);
  sensor_data.advertise(obs_publisher);
}

void loop()
{
  obs_data.data[0] = hc1.dist();
  obs_publisher.publish( &obs_data );
  sensor_data.spinOnce();
  delay(150);
}
