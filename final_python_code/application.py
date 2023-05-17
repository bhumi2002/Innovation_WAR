# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import Popen,PIPE
import rospy
from geometry_msgs.msg import Twist

rospy.init_node ('shield_open')
speed=Twist()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)  
speed.linear.x=0
speed.angular.z=0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(785, 651)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 230, 121, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 250, 101, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 370, 101, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 250, 111, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 130, 101, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 20, 181, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(560, 20, 181, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(560, 100, 181, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(50, 450, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(190, 450, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(190, 500, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(50, 500, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(50, 550, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(190, 550, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(190, 600, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(50, 600, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setStyleSheet("background:navy;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(610, 530, 101, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setStyleSheet("background:red;\n"
"color:white;\n"
"border-width:1.5px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.pushButton_17.setObjectName("pushButton_17")
        
        self.pushButton_17.clicked.connect(self.quit_master)
        self.pushButton_16.clicked.connect(self.drawer3_open_f)
        self.pushButton_15.clicked.connect(self.drawer3_close_f)
        self.pushButton_14.clicked.connect(self.drawer2_close_f)
        self.pushButton_13.clicked.connect(self.drawer2_open_f)
        self.pushButton_12.clicked.connect(self.drawer1_open_f)
        self.pushButton_11.clicked.connect(self.drawer1_close_f)
        self.pushButton_10.clicked.connect(self.drawer0_close_f)
        self.pushButton_9.clicked.connect(self.drawer0_open_f)
        self.pushButton_8.clicked.connect(self.protection_shield_close_f)
        self.pushButton_7.clicked.connect(self.protection_shield_open_f)
        self.pushButton_6.clicked.connect(self.Fire_extinguisher_f)
        self.pushButton_5.clicked.connect(self.forward_f)
        self.pushButton_4.clicked.connect(self.left_f)
        self.pushButton_3.clicked.connect(self.backward_f)
        self.pushButton_2.clicked.connect(self.right_f)
        self.pushButton.clicked.connect(self.stop)
                
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.roscore()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "stop"))
        self.pushButton_2.setText(_translate("Dialog", "right"))
        self.pushButton_3.setText(_translate("Dialog", "backward"))
        self.pushButton_4.setText(_translate("Dialog", "left"))
        self.pushButton_5.setText(_translate("Dialog", "forward"))
        self.pushButton_6.setText(_translate("Dialog", "Fire extinguisher"))
        self.pushButton_7.setText(_translate("Dialog", "protection shield open"))
        self.pushButton_8.setText(_translate("Dialog", "protection shield close"))
        self.pushButton_9.setText(_translate("Dialog", "drawer0 open"))
        self.pushButton_10.setText(_translate("Dialog", "drawer0 close"))
        self.pushButton_11.setText(_translate("Dialog", "drawer1 close"))
        self.pushButton_12.setText(_translate("Dialog", "drawer1 open"))
        self.pushButton_13.setText(_translate("Dialog", "drawer2 open"))
        self.pushButton_14.setText(_translate("Dialog", "drawer2 close"))
        self.pushButton_15.setText(_translate("Dialog", "drawer3 close"))
        self.pushButton_16.setText(_translate("Dialog", "drawer3 open"))
        self.pushButton_17.setText(_translate("Dialog", "quit"))

    def roscore(self):
        cmd="roscore"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> starting roscore") 
        cmd="python3 joystick.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> starting teleoperation") 

    def quit_master(self):
        cmd="killall -9 rosmaster"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> stopping roscore")          

    def Fire_extinguisher_f(self):
        cmd="python3 fire_extinguisher.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> fire_extinguiser")          

    def right_f(self):
        speed.linear.x=0.5
        speed.angular.z=1.0
        pub.publish(speed)
        print("--> right turn")   
        
    def backward_f(self):
        speed.linear.x=-1.0
        speed.angular.z=0.0
        pub.publish(speed)
        print("--> backward")   
        
    def left_f(self):
        speed.linear.x=0.5
        speed.angular.z=-1.0
        pub.publish(speed)
        print("--> left turn")  

    def forward_f(self):
        speed.linear.x=1.0
        speed.angular.z=0.0
        pub.publish(speed)
        print("--> forward")   

    def protection_shield_open_f(self):
        cmd="python3 shield_open.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> shield_open")  

    def protection_shield_close_f(self):
        cmd="python3 shield_close.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> shield_close")  

    def drawer0_close_f(self):
        cmd="python3 drawer0_close.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> drawer0_close")  

    def drawer1_close_f(self):
        cmd="python3 drawer1_close.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> drawer1_close") 
        
    def drawer2_close_f(self):
        cmd="python3 drawer2_close.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> drawer2_close") 

    def drawer3_close_f(self):
        cmd="python3 drawer3_close.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> drawer3_close") 

    def drawer0_open_f(self):
        cmd="python3 drawer0_open.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> drawer0_open") 

    def drawer1_open_f(self):
        cmd="python3 drawer1_open.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> drawer1_open") 

    def drawer2_open_f(self):
        cmd="python3 drawer2_open.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> drawer2_open") 

    def drawer3_open_f(self):
        cmd="python3 drawer3_open.py"
        Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        print("--> drawer3_open") 
        
    def stop(self):
        speed.linear.x=0.0
        speed.angular.z=0.0
        pub.publish(speed)
        print("--> stop") 
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
