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
 
 
# the meat
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

try:
    duration = int(sys.argv[1])
    if len(sys.argv)==3:
         duration=duration+0.5
    end_time = time.time() + duration
    while time.time() < end_time:
        spinreverse()
        elapsed=int((time.time()-end_time)*-1)
        #print(elapsed)
        with open("number.txt","w") as file:
             file.write(str(elapsed))
except KeyboardInterrupt:
    cleanup()
    exit( 1 )
 
cleanup()
exit( 0 )
