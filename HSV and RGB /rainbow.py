import cv2

import numpy as np

black1=np.zeros([256,180,3],dtype=np.uint8)

black2=np.zeros([256,180,3],dtype=np.uint8)




cv2.imshow("black image ",black1)



for y in range(0,256,1):
    for x in range(0,180,1):
        black1[y,x]=(x,y,255)

black1=cv2.resize(black1,(500,500))

black1=cv2.cvtColor(black1,cv2.COLOR_HSV2BGR)

cv2.imshow("picture 1",black1)

for y in range(0,256,1):
    for x in range(0,180,1):
        black2[y,x]=(x,255,y)

black2=cv2.cvtColor(black2,cv2.COLOR_HSV2BGR)

black2=cv2.resize(black2,(500,500))

cv2.imshow("picture 2",black2)
