#!/bin/bash

# Check if motor.py is running
if pgrep -f motor.py > /dev/null; then
  # If it is, terminate it
  pkill -f motor.py
  echo "motor.py terminated"
  pkill -f ~/Adafruit_Python_SSD1306/examples/counting.py
  python ~/Adafruit_Python_SSD1306/examples/Display.py "Estop Pressed"
  exit 0
else
  echo "motor.py is not running"
fi

#Check if motorreverse.py is runnnig
if pgrep -f motorreverse.py > /dev/null; then
  # If it is, terminate it
  pkill -f motorreverse.py
  echo "motorreverse.py terminated"
  exit 0
else
  echo "motorreverse.py is not running"
fi


python motorstartup.py

number=$(cat number.txt)
if [ "$number" -ne 0 ]; then
  number=$((number))
  echo "$number"
  python ~/Adafruit_Python_SSD1306/examples/Display.py "Recovering"
  python motorreverse.py $number 1
  echo "0" > number.txt
  echo "recovery complete"
  python ~/Adafruit_Python_SSD1306/examples/StartUp.py
  
  exit 0
fi


sudo dhclient -v wlan0

adb devices

python speech.py

/usr/lib/android-sdk/platform-tools/aarun.sh

sudo python play_sound.py

number=$(cat output.txt)

number=$(( (${#number} - 1) * 5 ))

python ~/Adafruit_Python_SSD1306/examples/counting.py $number &

python motor.py

python ~/Adafruit_Python_SSD1306/examples/Display.py "Resetting"

sleep  $number

python ~/Adafruit_Python_SSD1306/examples/StartUp.py 

while true
do
    if pgrep -f motor.py > /dev/null
    then
        :
    else
        python ~/Adafruit_Python_SSD1306/examples/StartUp.py 
    fi
    exit 0
done
