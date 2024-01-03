import cv2

import numpy as np

def mouse(event,x,y,flag,param):
    global EVENT
    global xPos
    global yPos

    if event==cv2.EVENT_LBUTTONDOWN:
        EVENT=event
        xPos=x
        yPos=y

    if event==cv2.EVENT_LBUTTONUP:
        EVENT = event
        xPos = x
        yPos = y

height=780
width=1500

H=28
W=(1500/780)*28
EVENT=0

camera=cv2.VideoCapture(0)

cv2.namedWindow("hello")
cv2.setMouseCallback("hello",mouse)


while True:
    ignore,frame=camera.read()

    output_frame=cv2.resize(frame,(width,height))

    if EVENT==1:
        black=np.zeros([250,250,3],dtype=np.uint8)

        #black_HSV=cv2.cvtColor(black,cv2.COLOR_BGR2HSV)



        #frame_HSV=cv2.cvtColor(output_frame,cv2.COLOR_BGR2HSV)

        color_pick=output_frame[yPos,xPos]
        
  

        black[:,:]=color_pick

        cv2.putText(black,str(color_pick),(10,100),cv2.FONT_HERSHEY_COMPLEX,1,(100,50,0),3)

        cv2.imshow("desired color",black)

        print(xPos," ",yPos)

        #print("cordinates are : ",(abs(width*0.5-xPos)(W/width),abs(height*0.5-yPos)(H/height)),"in cm")

        
        


    cv2.imshow("hello",output_frame)

    

    if cv2.waitKey(1)==ord("a"):
        break
