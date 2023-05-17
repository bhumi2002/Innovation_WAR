#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32MultiArray

pwm1=Int32MultiArray()
pwm1.data=[0,0]

def callback(msg):
	print (msg)
	left=msg.linear.x+msg.angular.z
	right=msg.linear.x-msg.angular.z
	pwm1.data[0]=int((left+1)*510/2)
	pwm1.data[1]=int((right+1)*510/2)
	pub.publish(pwm1)	
	
rospy.init_node('joystick')
pub = rospy.Publisher('/pwm', Int32MultiArray,queue_size=10)
sub =  rospy.Subscriber('/cmd_vel', Twist, callback)
rospy.spin()

