import tkinter as tk   
from tkinter import *
import rospy
from std_msgs.msg import Int32MultiArray
import time

prev1=0
prev2=0
prev3=0
prev4=0

win = tk.Tk()
win.geometry("750x250")

rospy.init_node ('module')
M=Int32MultiArray()
pub = rospy.Publisher('/Don', Int32MultiArray, queue_size=1)  
M.data=[0,0,0]

def fire_extinguisher_f():
    M.data=[4,1,255] # pwm=255
    pub.publish(M)
    time.sleep(7)  #delay time 
    M.data=[4,1,0]
    pub.publish(M) 
    M.data=[9,1,255] #servo motor
    pub.publish(M)
    time.sleep(1)
    M.data=[9,0,255]
    pub.publish(M)
    time.sleep(1)
    M.data=[9,0,0]
    pub.publish(M)
    
def protection_system_on_f():
    M.data=[8,1,255] # pwm=255
    pub.publish(M)
    time.sleep(7)  #delay time 
    M.data=[8,1,0] # pwm=255
    pub.publish(M)
    
def protection_system_off_f():
    M.data=[8,0,255] # pwm=255
    pub.publish(M)
    time.sleep(7)  #delay time 
    M.data=[8,0,0] # pwm=255
    pub.publish(M)
    
def left_upper_drawer_f():
    global prev1
    if((sli1.get()-prev1)>0):
        M.data=[0,1,87]
    elif((sli1.get()-prev1)<0):
        M.data=[0,0,87]
    else:
        M.data=[0,0,0]
    pub.publish(M)
    time.sleep(abs(sli1.get()-prev1))  #delay time 
    M.data=[0,0,0] # pwm=255
    pub.publish(M) 
    prev1=sli1.get()
       
def left_lower_drawer_f():
    global prev2
    if((sli1.get()-prev2)>0):
        M.data=[1,1,87]
    elif((sli1.get()-prev2)<0):
        M.data=[1,0,87]
    else:
        M.data=[1,0,0]
    pub.publish(M)
    time.sleep(abs(sli1.get()-prev2))  #delay time 
    M.data=[1,0,0] # pwm=255
    pub.publish(M) 
    prev2=sli1.get()
    
def right_upper_drawer_f():
    global prev3
    if((sli1.get()-prev3)>0):
        M.data=[2,1,87]
    elif((sli1.get()-prev3)<0):
        M.data=[2,0,87]
    else:
        M.data=[2,0,0]
    pub.publish(M)
    time.sleep(abs(sli1.get()-prev3))  #delay time 
    M.data=[2,0,0] # pwm=255
    pub.publish(M) 
    prev3=sli1.get()
    
def right_lower_drawer_f():
    global prev4
    if((sli1.get()-prev4)>0):
        M.data=[3,1,87]
    elif((sli1.get()-prev4)<0):
        M.data=[3,0,87]
    else:
        M.data=[3,0,0]
    pub.publish(M)
    time.sleep(abs(sli1.get()-prev4))  #delay time 
    M.data=[3,0,0] # pwm=255
    pub.publish(M) 
    prev4=sli1.get()

fire_extinguisher = tk.Button(win,text="fire_extinguisher",command=fire_extinguisher_f)
protection_system_on = tk.Button(win,text="protection_system_on",command=protection_system_on_f)
protection_system_off = tk.Button(win,text="protection_system_off",command=protection_system_off_f)
left_upper_drawer=tk.Button(win,text="send1",command=left_upper_drawer_f)
left_lower_drawer=tk.Button(win,text="send2",command=left_lower_drawer_f)
right_upper_drawer=tk.Button(win,text="send3",command=right_upper_drawer_f)
right_lower_drawer=tk.Button(win,text="send4",command=right_lower_drawer_f)

sli1 = tk.Scale(win, from_=0, to=100,length=200,orient=HORIZONTAL)
sli1.place(relx=0.15,rely=0.06,relwidth=10)
fire_extinguisher.grid(row=5, column=10)
protection_system_on.grid(row=7, column=9)
protection_system_off.grid(row=7, column=11)
sli1.grid(row=10,column=10)
left_upper_drawer.grid(row=9, column=9)
left_lower_drawer.grid(row=11, column=9)
right_upper_drawer.grid(row=9, column=11)
right_lower_drawer.grid(row=11, column=11)

win.mainloop()
