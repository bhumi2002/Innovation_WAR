
import rospy
import tf
from std_msgs.msg import Int32MultiArray
msg="""Which motor you want to control :

0. Drawer0
1. Drawer1
2. Drawer2
3. Drawer3
4. fire extinguisher
5. robotic arm stepper1
6. robotic arm stepper2
7. robotic arm stepper3
8. shield motor
9. fire extinguisher servo
10. jhonson motor for fire extinguisher
11. linear actuator (robotic arm)

"""

rospy.init_node ('Don')
M=Int32MultiArray()
pub = rospy.Publisher('/Don', Int32MultiArray, queue_size=1)  
M.data=[0,0,0]   #0=motor 1=dir,2=pwm
if __name__ == '__main__':
    while(1):
        print(msg)
        motor=int(input('motor : '))
        M.data[0]=motor
        direction=int(input('direction : '))
        M.data[1]=direction
        pwm=int(input('pwm : '))
        M.data[2]=pwm
        pub.publish(M)
