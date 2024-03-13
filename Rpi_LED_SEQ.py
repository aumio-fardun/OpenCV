import RPi.GPIO as GP

import time


def BINARY(n):
    bin = ""

    bin_list = []

    if n==0:
        bin_list=[0]

    elif n==1:
        bin_list=[1]


    while (n!=0 and 1 and int(n/2)>0):

        bin += str(n % 2)

        n = int(n / 2)

        if n == 1:
            bin += str(1)

    for i in range(len(bin) - 1, -1, -1):
        bin_list.append(int(bin[i]))

    return bin_list


def BITWISE(bits,number):

    null_0=[]

    for c in range(0,bits):

        null_0.append(0)

    binary_list=BINARY(number)

    diff=len(null_0)-len(binary_list)

    if diff!=0:

        binary_list.reverse()

        for j in range(0,diff):

            binary_list.append(0)

        binary_list.reverse()

    return binary_list



TOTAL_LED=int(input("enter number of leds : "))

TOTAL_SEQ=2**(TOTAL_LED)



RESULT_LIST=[]

for num in range (0,TOTAL_SEQ):

    per_list=BITWISE(TOTAL_LED,num)

    RESULT_LIST.append(per_list)

print(RESULT_LIST)


GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)
GP.setup(12,GP.OUT)
GP.setup(13,GP.OUT)
GP.setup(15,GP.OUT)
GP.setup(16,GP.OUT)
GP.setup(18,GP.OUT)
GP.setup(22,GP.OUT)
GP.setup(29,GP.OUT)
GP.setup(31,GP.OUT)
GP.setup(32,GP.OUT)

t=.2

for l in range(0,len(RESULT_LIST)):
  GP.output(11,RESULT_LIST[l][0])
  time.sleep(t)

  GP.output(12,RESULT_LIST[l][1])
  time.sleep(t)

  GP.output(13,RESULT_LIST[l][2])

  time.sleep(t)

  GP.output(15,RESULT_LIST[l][3])

  time.sleep(t)

  GP.output(16,RESULT_LIST[l][4])

  time.sleep(t)

  GP.output(18,RESULT_LIST[l][5])
  time.sleep(t)

  

  GP.output(22,RESULT_LIST[l][6])

  time.sleep(t)

  GP.output(29,RESULT_LIST[l][7])

  time.sleep(t)

  GP.output(31,RESULT_LIST[l][8])

  time.sleep(t)

  GP.output(32,RESULT_LIST[l][9])

  time.sleep(t)




  GP.output(11,0)
  GP.output(12,0)
  GP.output(13,0)
  GP.output(15,0)
  GP.output(16,0)
  GP.output(18,0)
  GP.output(22,0)
  GP.output(29,0)
  GP.output(31,0)
  GP.output(32,0)




GP.cleanup()
