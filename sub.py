#!/usr/bin/env python3
import serial,time


if __name__ == '__main__':
	rospy.init_node('topic_subscriber')
	sub = rospy.Subscriber('cmd_vel', Twist, callback)
	if __name__ == '__main__': 
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyACM0", 9600, timeout=1) as arduino:
        time.sleep(0.1) #wait for serial to open
        if arduino.isOpen():
            print("{} connected!".format(arduino.port))
            try:
                while True:
                    cmd=input("Enter command : ")
                    arduino.write(cmd.encode())
                    #time.sleep(0.1) #wait for arduino to answer
                    while arduino.inWaiting()==0: pass
                    if  arduino.inWaiting()>0: 
                        answer=arduino.readline()
                        print(answer)
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
	rospy.spin()

