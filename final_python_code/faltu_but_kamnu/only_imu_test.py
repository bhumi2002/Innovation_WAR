import rospy
import tf
from gazebo_msgs.msg import ModelStates
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Float32
import math
from math import atan2,sin,cos,asin,sqrt


# start is x:0, y:0 ,initial yaw angle of robot ----> initialization 
yaw=0.0  
global angle_to_goal

# goal-gps data
latitude=float(input('Enter latitude: '))
longitude=float(input('Enter longitude: '))

rospy.init_node ('subscriber')

# create publisher for send the velocity
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
speed=Twist()
        
# find yaw angle from imu data
def callback(msg):
    global yaw
    yaw=msg.data
    if(yaw<0):
        yaw=yaw+360
    
# distance and angle_of_the_goal           
def distance(msg):
    lat1=msg.latitude
    lon1=msg.longitude
    lat2=latitude
    lon2=longitude
    dy = lat2 - lat1
    dx = math.cos(3.14159/180*lat1)*(lon2 - lon1)
    global dist
    angle_to_goal = atan2(dy, dx)
    angle_to_goal = angle_to_goal*180/3.14
    radius = 6365.668 # km
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = (math.sin(dlat/2) * math.sin(dlat/2)) + (math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2))
    c = 2 * math.asin(math.sqrt(a))
    dist = radius * c*1000
    print("distance         ->    ",dist)
    
    # angle difference
    turn = angle_to_goal - yaw       
    
    # minimum angle turn
    if abs(turn)>180 :
        q=abs(turn)-180
        turn=-1*turn*q/abs(turn)
    
    print("Angle Difference ->    ",turn)
    
    
    # threshold turn (difference) = 0.05
    if abs(turn) < 15:   
        move_forward = True
    else: 
        # move with only angular velocity
        move_forward=False

        # direction of turn is depend on the sign of turn (difference)
        if turn<0:
            a=-0.3
            print('turn left')
        else:
            a=0.3
            print('turn right')
        speed.angular.z = abs(turn) * a /150 
        speed.linear.x=0

    if move_forward == True:
        print('forward')
        # move with only linear velocity
        # threshold distance = 2.0
        if dist>2.0:
            speed.linear.x=1.2
            speed.angular.z=0
        else:
            speed.linear.x=0
            speed.angular.z=0

def main():
    global angle_to_goal
    sub2=rospy.Subscriber('/imu_data',Float32 , callback)
    sub3 =rospy.Subscriber('/fix', NavSatFix,distance)
    
if __name__ == '__main__':
    main()
    rospy.Rate(5)
    rospy.spin()
