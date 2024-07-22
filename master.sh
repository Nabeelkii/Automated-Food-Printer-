#!/bin/bash

# Check if motor.py is running
if pgrep -f motor.py > /dev/null; then
  # If it is, terminate it
  pkill -f motor.py
  echo "motor.py terminated"
  exit 0
else
  echo "motor.py is not running"
fi

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
  python motorreverse.py $number 1
  echo "0" > number.txt
  echo "recovery complete"
  exit 0
fi


sudo dhclient -v wlan0

adb devices

python speech.py

/usr/lib/android-sdk/platform-tools/aarun.sh

sudo python play_sound.py

python motor.py &

number=$(cat output.txt)

number=$(( (${#number} - 1) * 5 ))

python ~/Adafruit_Python_SSD1306/examples/counting.py number

