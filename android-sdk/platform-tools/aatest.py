import sys
import time
from ppadb.client import Client as AdbClient
if len(sys.argv) < 1:
        print("Not enough args")
        sys.exit(1)

PHONEIP = sys.argv[1]


try:
    file_path = '/home/raspi6/output.txt'
    with open(file_path, 'r') as file:
        input = file.read()
        print(f"input:{input}")
except FileNotFoundError:
    input = 'hello'

client = AdbClient(host="127.0.0.1", port=5037)
device = client.device(PHONEIP)

#get width and height
phonesize=device.shell('wm size')
#print(f"Phonesize from python:{phonesize}")
width=""
height=""
for i in range(len(phonesize)): #extract ip address
        if(phonesize[i]=='x'): #24 is first \n
            width+=phonesize[i-4]
            width+=phonesize[i-3]
            width+=phonesize[i-2]
            width+=phonesize[i-1]
            height+=phonesize[i+1]
            height+=phonesize[i+2]
            height+=phonesize[i+3]
            height+=phonesize[i+4]

'''
print(f"IP from python:{PHONEIP}")
print(f"Phonewidth from python:{width}")
print(f"Phoneheight from python:{height}")
'''
#print(f"Input:{input}")
#clearscreen
pos1=str(int(width)-100)
pos2=str((int(height)/25)*10-100)
keyboard='input tap ' + pos1+' '+ pos2
device.shell(keyboard)
time.sleep(.5)
pos1=str(int(width)-200)
pos2=str((int(height)/25)*14)
keyboard='input tap ' +pos1 +' ' +pos2
device.shell(keyboard)
time.sleep(.5)

#Press the edit text button
pos1=str(((int(width))/6)*2)
pos2=str((int(height)/25)*11)
keyboard='input tap ' + pos1+ ' ' + pos2
device.shell(keyboard)
time.sleep(.5)

words = input.split()

for word in words:
    text='input text ' + word 
    device.shell(text)
    device.shell("input keyevent 62")
    
pos1=str(int(width)-100)
pos2=str((int(height)/25)*11)
keyboard='input tap ' + pos1+' '+ pos2 
device.shell(keyboard) #enter command into keyboard
pos1=str(int(width)/2)
pos2=str((int(height)/25)*22)
keyboard='input tap ' + pos1+' ' +pos2
time.sleep(1)
device.shell(keyboard) #press print button

