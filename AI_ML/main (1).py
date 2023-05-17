import cv2
import rospy
import numpy as np
import matplotlib.pyplot as plt
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Int32

net = cv2.dnn.readNetFromDarknet("/home/user/EC_plan/AI_ML/yolo-tiny-obj.cfg","/home/user/EC_plan/AI_ML/yolo-tiny-obj.weights")

classes = ['Drons','jet', 'tank','military vehicle','military bases','Pistol','Guns','Knife','Grenade','Army']


rospy.init_node ('ML')

# create publisher for send the velocity
pub = rospy.Publisher('/ml_detection', Int32, queue_size=1)

#cap = cv2.VideoCapture(2)
bridge=CvBridge()
def chali_ja(msg):
    data=Int32()
    #_, img = cap.read()
    #print(msg)
    img=bridge.imgmsg_to_cv2(msg, "bgr8")
    #img=msg.data
    #print(img)
    #while(_ is False):
    #    _,img=cap.read()
    img = cv2.resize(img,(1280,720))
    hight,width,_= img.shape
    blob = cv2.dnn.blobFromImage(img, 1/255,(416,416),(0,0,0),swapRB = True,crop= False)
    #blob = msg.data
    #print(blob)
    net.setInput(blob)

    output_layers_name = net.getUnconnectedOutLayersNames()

    layerOutputs = net.forward(output_layers_name)

    boxes =[]
    confidences = []
    class_ids = []
    print('-1')
    for output in layerOutputs:
        for detection in output:
            score = detection[5:]
            class_id = np.argmax(score)
            confidence = score[class_id]
            if confidence > 0.7:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * hight)
                w = int(detection[2] * width)
                h = int(detection[3]* hight)
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)


    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.5,.4)

    boxes =[]
    confidences = []
    class_ids = []
    print('0')
    for output in layerOutputs:
        for detection in output:
            score = detection[5:]
            class_id = np.argmax(score)
            confidence = score[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * hight)
                w = int(detection[2] * width)
                h = int(detection[3]* hight)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x,y,w,h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)
    print('1')
    indexes = cv2.dnn.NMSBoxes(boxes,confidences,.8,.4)
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0,255,size =(len(boxes),3))
    if  len(indexes)>0:
        for i in indexes.flatten():
            x,y,w,h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            color = colors[i]
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,label + " " + confidence, (x,y+400),font,2,color,2)

    cv2.imshow('img',img)
    plt.imshow(img, cmap='gray')
    plt.show()
    print(class_ids)
    print(boxes)
    print(confidence)
    if(class_ids):
        data.data=class_ids[0]
    else:
        data.data=-1
    pub.publish(data)
    #if cv2.waitKey(1) == ord('q'):
        #break
if __name__ == '__main__':
    sub1=rospy.Subscriber('/usb_cam/image_raw',Image,chali_ja)
    rospy.spin()
#cap.release()
#cv2.destroyAllWindows()
