import rospy
import tf
from std_msgs.msg import Int32MultiArray
import time

rospy.init_node ('Fire_extinguisher')
M=Int32MultiArray()
pub = rospy.Publisher('/Don', Int32MultiArray, queue_size=1)  
M.data=[0,0,0]
time.sleep(0.1)
M.data=[4,1,255] # pwm=255
pub.publish(M)
time.sleep(7)  #delay time 
M.data=[4,1,0]
time.sleep(0.1)
pub.publish(M) 
M.data=[9,1,255] #servo motor
time.sleep(0.1)
pub.publish(M)
time.sleep(1)
M.data=[9,0,255]
pub.publish(M)
time.sleep(1)
M.data=[9,0,0]
pub.publish(M)
time.sleep(0.1)

