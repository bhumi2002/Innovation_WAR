#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import serial,time

def callback(msg):
	left=msg.linear.x+(msg.angular.z)
	right=msg.linear.x-(msg.angular.z)
    if (abs(left)>2):
        if (sign(left)==1):
            left=2
        if (sign(left)==-1):
            left= -2
    if (abs(right)>2):
        if (sign(right)==1):
            right=2
        if (sign(right)==-1):
            right=-2
    PWM1_value = ((left/2)*255)+255
    arduino.write(str(PWM1_value).encode())
    PWM2_value = ((right/2)*255)+255
    arduino.write(str(PWM2_value).encode())



	
if _name_ == '_main_':
    
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
		            sub =  rospy.Subscriber('cmd_vel', Twist, callback)
                except KeyboardInterrupt:
                    print("KeyboardInterrupt has been caught.")