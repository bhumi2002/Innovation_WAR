import rospy
import tf
from std_msgs.msg import Int32MultiArray
import time

rospy.init_node ('d2_open')
M=Int32MultiArray()
pub = rospy.Publisher('/Don', Int32MultiArray, queue_size=1)  
M.data=[0,0,0]
time.sleep(1)
M.data=[2,1,50] # pwm=255
pub.publish(M)
time.sleep(3)  #delay time 
M.data=[2,1,0]
pub.publish(M) 
