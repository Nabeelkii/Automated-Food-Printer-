![Picture of product](https://github.com/Nabeelkii/Automated-Food-Printer/blob/master/Readme/Product.jpg?raw=true)
Steps to replicate the project:

Install this OS on raspberry pi:
Raspberry Bullseye 64bit

You will need the following 2 packages for this project to work:<br />
ADB<br />
Speech Recognition<br />

Below are the steps to install both packages

Next install adb:

sudo apt install adb 
mkdir cli-tools
wget -c https://dl.google.com/android/repository/platform-tools-latest-linux.zip
unzip platform-tools-latest-linux.zip 
cd platform-tools/

Test that the package is working using the command:
```
adb devices
```
if this does not work download the raw folder from this website:
https://pypi.org/project/pure-python-adb/

Place the folder inside the raspberry pi

Run the above command again to test if it is working
Note that your directory needs to be inside the adb package to be able to execute the command

adb requires the ip address of the phone to run,the shell script aarun extracts the ip address of the connected phone and runs the script

run adb using:
```
./aarun.sh
```


Next install speech to text:
```
pip install SpeechRecognition
sudo apt-get install -y python3-pyaudio
sudo apt-get install flac
```
Use this command to check card number of audio device:
```
arecord -l
```
Use this command to change the card number according to the card number:
sudo nano /use/share/alsa/alsa.conf

Run speech.py using:
```
python speech.py
```

The raspberry pi needs to be connected to the internet for the package to work
Check for internet connection using:
```
ping -c 4 8.8.8.8
```
Motor being used is L298N connected to a NIMA17
Connect the raspberry pi GPIO pins to the L298N board as shown below:
IN1:17
IN2:18
IN3:27
IN4:22
ENA:6
ENB:13

Run the following command to startup the motor:
```
python motorstartup.py
```
Run the following command to test the motor(the 10 at the end defines how many seconds to move the motor):
```
python motorforward.py 10     
python motorreverse.py 10
```

Connect the tact switch to Bcm pin 25

Run the following command to start the overall program:
```
python controller.py
```
Press the button to start program
