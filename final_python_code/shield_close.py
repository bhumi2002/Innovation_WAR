import rospy
import tf
from std_msgs.msg import Int32MultiArray
import time

rospy.init_node ('shield_close')
M=Int32MultiArray()
pub = rospy.Publisher('/Don', Int32MultiArray, queue_size=1)  
M.data=[0,0,0]
time.sleep(1)  #delay time 
M.data=[8,0,255]
pub.publish(M) 
time.sleep(7)  #delay time 
M.data=[8,0,0]
pub.publish(M) 
