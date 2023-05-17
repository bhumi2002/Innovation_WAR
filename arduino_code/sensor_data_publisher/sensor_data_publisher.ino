
#include "MPU9250.h"
#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <std_msgs/Float32.h>
#include <HCSR04.h>

ros::NodeHandle sensor_data;
MPU9250 mpu;

//-----------------------------------------------HCSR04 pin define - initialisation class HCSR04 (trig pin , echo pin)
#define e1 10
#define t1 9
#define e2 31
#define t2 29
#define e3 51
#define t3 49
#define e4 A13
#define t4 A12
#define e5 A9
#define t5 A10

HCSR04 hc1(t1, e1);
HCSR04 hc2(t2, e2); 
HCSR04 hc3(t3, e3);   
HCSR04 hc4(t4, e4);   
HCSR04 hc5(t5, e5);  

//-----------------------------------------------TG pin define (TG = [Temperature, gas])
#define temperature_pin A3
#define gas_sensor_pin A0
int val; 

//-----------------------------------------------Publisher for HCSR04_data, IMU_data, TG_data
std_msgs::Float32MultiArray obs_data;
ros::Publisher obs_publisher("obs_data", &obs_data);

std_msgs::Float32 imu_data;
ros::Publisher imu_publisher("imu_data", &imu_data);

std_msgs::Float32MultiArray TG_data;                 
ros::Publisher TG_publisher("TG_data", &TG_data);

//-----------------------------------------------void setup()
void setup()
{
  Serial.begin(57600);
  Wire.begin();
  sensor_data.getHardware()->setBaud(57600);
  sensor_data.initNode();

  pinMode(temperature_pin, INPUT);
  pinMode(gas_sensor_pin, INPUT);
  
  obs_data.data_length = 5;
  obs_data.data = (float *)malloc((sizeof(float))*obs_data.data_length * 2);
  TG_data.data_length = 2;
  TG_data.data = (float *)malloc((sizeof(float))*TG_data.data_length * 2);
  
  sensor_data.advertise(obs_publisher);
  sensor_data.advertise(imu_publisher);
  sensor_data.advertise(TG_publisher);
  
  if (!mpu.setup(0x68)) {  // change to your own address
     while (1) {
            delay(5000);
     }
  }

  delay(5000);
  mpu.calibrateMag();
  mpu.verbose(false);
}

void loop()
{
  //-----------------------------------------------HCSR04 data publish
  obs_data.data[0] = hc1.dist();
  obs_data.data[1] = hc2.dist();
  obs_data.data[2] = hc3.dist();
  obs_data.data[3] = hc4.dist();
  obs_data.data[4] = hc5.dist();
  obs_publisher.publish( &obs_data );

  //-----------------------------------------------imu data publish
  delay(15);
  if (mpu.update()) {
     static uint32_t prev_ms = millis();
       if (millis() > prev_ms + 25) {
          imu_data.data = mpu.getYaw();
          imu_publisher.publish( &imu_data );
          delay(150);
          prev_ms = millis();
       }
  }

  //----------------------------------------------Temperature , pressure and gas sensor data publish
  val = analogRead(temperature_pin);
  float mv = ( val/1024.0)*5000;
  float cel = mv/10;
  TG_data.data[0]=cel;
  TG_data.data[2]=analogRead(gas_sensor_pin);
  TG_publisher.publish( &TG_data );

  sensor_data.spinOnce();
  
}
