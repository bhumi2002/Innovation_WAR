#include "MPU9250.h"
#include <ros.h>
#include <std_msgs/Float32.h>
ros::NodeHandle  nh;
MPU9250 mpu;

std_msgs::Float32 str_msg;
ros::Publisher chatter("imu_data", &str_msg);
void setup() {
    Serial.begin(9600);
    Wire.begin();
    delay(2000);
    nh.getHardware()->setBaud(9600);
    nh.initNode();
    nh.advertise(chatter);
    if (!mpu.setup(0x68)) {  // change to your own address
        while (1) {
            delay(5000);
        }
    }

    delay(5000);
    mpu.calibrateMag();
    mpu.verbose(false);
}

void loop() {
    if (mpu.update()) {
        static uint32_t prev_ms = millis();
        if (millis() > prev_ms + 25) {
            //print_roll_pitch_yaw();
            str_msg.data = mpu.getYaw();
            Serial.println(str_msg.data);
            chatter.publish( &str_msg );
            nh.spinOnce();
            delay(150);
            prev_ms = millis();
        }
    }
}
