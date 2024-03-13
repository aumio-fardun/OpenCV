x=[]

for i in range(0,21):
    x.append(i)

y1=[5*p for p in x]

x.reverse()

y2=[5*p for p in x]


print(y1)

print(y2)


import time

import RPi.GPIO as GP

GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)
GP.setup(12,GP.OUT)
GP.setup(13,GP.IN)

a1=GP.PWM(11,100)
a2=GP.PWM(12,100)

a1.start(0)
a2.start(0)

count=0

try:
   while True:
       val=GP.input(13)
       

       if val==0:

        a1.ChangeDutyCycle(0)
        a2.ChangeDutyCycle(0)

       elif val==1:


            if count%2==0:
             
             

             for DC1,DC2 in zip(y1,y2):

               a1.ChangeDutyCycle(DC1)
               a2.ChangeDutyCycle(DC2)
               time.sleep(.07)
             count+=1

 


            elif count%2!=0:
 
             for DC1,DC2 in zip(y1,y2):

                a1.ChangeDutyCycle(DC2)
                a2.ChangeDutyCycle(DC1)
                time.sleep(.07)

             count+=1



except KeyboardInterrupt:
       
       Gp.cleanup()
