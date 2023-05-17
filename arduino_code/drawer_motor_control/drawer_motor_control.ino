#include <ros.h>
#include <std_msgs/Int32MultiArray.h>
ros::NodeHandle module_node;

std_msgs::Int32MultiArray m;

int drawer_dir[4]={7,8,9,10};
int drawer_pwm[4]={3,4,5,6};

void module(const std_msgs::Int32MultiArray& m){

        if(m.data[0]==1){
              digitalWrite(drawer_dir[m.data[1]],HIGH);
              analogWrite(drawer_pwm[m.data[1]],85);
        }else if(m.data[0]==5){
              digitalWrite(drawer_dir[m.data[1]],HIGH);
              analogWrite(drawer_pwm[m.data[1]],0);          
        }else if(m.data[0]==6){
              digitalWrite(drawer_dir[m.data[1]],LOW);
              analogWrite(drawer_pwm[m.data[1]],85); 
        }

}

ros::Subscriber<std_msgs::Int32MultiArray> module_sub("Don", &module );
void setup() {
  Serial.begin(57600);
  pinMode(drawer_dir[0], OUTPUT);
  pinMode(drawer_dir[1], OUTPUT);
  pinMode(drawer_dir[2], OUTPUT);
  pinMode(drawer_dir[3], OUTPUT);

  pinMode(drawer_pwm[0], OUTPUT);
  pinMode(drawer_pwm[1], OUTPUT);
  pinMode(drawer_pwm[2], OUTPUT);
  pinMode(drawer_pwm[3], OUTPUT);

  module_node.getHardware()->setBaud(57600);
  module_node.initNode();
  module_node.subscribe(module_sub);

}

void loop() {
  module_node.spinOnce();
  delay(1);
}
