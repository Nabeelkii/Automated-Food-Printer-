#!/usr/bin/python3
import RPi.GPIO as GPIO
import sys
import time
 
out1 = 17
out2 = 27
out3 = 22
out4 = 23
 
# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.001
 
step_count = 200
 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( out1, GPIO.OUT )
GPIO.setup( out2, GPIO.OUT )
GPIO.setup( out3, GPIO.OUT )
GPIO.setup( out4, GPIO.OUT )
GPIO.setup( 6, GPIO.OUT )
GPIO.setup( 13, GPIO.OUT )
 
# initializing
GPIO.output( out1, GPIO.LOW )
GPIO.output( out2, GPIO.LOW )
GPIO.output( out3, GPIO.LOW )
GPIO.output( out4, GPIO.LOW )
 
 
def cleanup():
    GPIO.output( out1, GPIO.LOW )
    GPIO.output( out2, GPIO.LOW )
    GPIO.output( out3, GPIO.LOW )
    GPIO.output( out4, GPIO.LOW )
    GPIO.cleanup()
 
 
def spinforward():
    i = 0
    for i in range(step_count):
        if i%4==0:
            GPIO.output( out4, GPIO.HIGH )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.HIGH )
            GPIO.output( out1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.HIGH )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.HIGH )
 
        time.sleep( step_sleep )

def spinreverse():
    i = 0
    for i in range(step_count):
        if i%4==0:
            GPIO.output( out4, GPIO.HIGH )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.HIGH )
            GPIO.output( out1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.HIGH )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( out4, GPIO.LOW )
            GPIO.output( out3, GPIO.LOW )
            GPIO.output( out2, GPIO.LOW )
            GPIO.output( out1, GPIO.HIGH )
 
        time.sleep( step_sleep )

elapsed=0

try:    
    file = open('/home/raspi6/output.txt','r')
    content = file.read()
    wordlen=len(content)-1
    print(wordlen)
    duration = wordlen*5
    print(duration)
    if (duration>40):
        duration=42
    #duration = int(sys.argv[1])
    end_time = time.time() + duration
    print("going forward")
    while time.time() < end_time:
        spinforward()
        elapsed=int((time.time()-end_time)+duration)
        #print(elapsed)
        with open("number.txt", "w") as file:
            file.write(str(elapsed))
    end_time=time.time()+duration
    print("going reverse")
    while time.time() < end_time:
        spinreverse()
        elapsed=(time.time()-end_time)
        elapsed=int(elapsed*-1)
        #print(elapsed)
        with open("number.txt", "w") as file:
            file.write(str(elapsed))

except KeyboardInterrupt:
    cleanup()
    exit( 1 )
 
cleanup()
exit( 0 )
sys.exit()
