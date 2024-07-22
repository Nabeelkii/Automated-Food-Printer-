![Picture of product](https://github.com/Nabeelkii/Automated-Food-Printer/blob/master/Readme/Product.jpg?raw=true)
Steps to replicate the project:

Install this OS on raspberry pi:
Raspberry Bullseye 64bit

You will need the following 2 packages for this project to work:<br />
ADB<br />
Speech Recognition<br />

Below are the steps to install both packages

Steps to install adb:
```
sudo apt install adb 
mkdir cli-tools
wget -c https://dl.google.com/android/repository/platform-tools-latest-linux.zip
unzip platform-tools-latest-linux.zip 
cd platform-tools/
```
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

Run adb using:
```
./aarun.sh
```


Steps to install SpeechRecognition:
```
pip install SpeechRecognition==3.8.1
sudo apt-get install -y python3-pyaudio
sudo apt-get install flac
```
Use this command to check card number of audio device:
```
arecord -l
```
Use this command to change the card number according to the card number:
```
sudo nano /use/share/alsa/alsa.conf
```
Run speech.py using:
```
python speech.py
```

The raspberry pi needs to be connected to the internet for the above command to work


Check for internet connection using:

```
ping -c 4 8.8.8.8
```
If there is no connection, try the below command to refresh the connection:
```
sudo dhclient -v wlan0
```

Motor being used is L298N connected to a NIMA17<br />
Connect the raspberry pi GPIO pins to the L298N board as shown below:<br />
IN1:17<br />
IN2:18<br />
IN3:27<br />
IN4:22<br />
ENA:6<br />
ENB:13<br />

The ENA pin needs to be connected and set to high in order for the motor to work. 

Run the following command to startup the motor:
```
python motorstartup.py
```
Run the following command to test the motor(the 10 at the end defines how many seconds to move the motor):
```
python motorforward.py 10     
python motorreverse.py 10
```

Connect the tact switch to Bcm pin 25, power to pin 1, and the other to ground

Finally to setup the speaker:<br />
Amp Vin to Raspbery Pi 5V Power<br />
Amp GND to Raspbery Pi Ground<br />
Amp DIN to Raspbery Pi GPIO 21<br />
Amp BCLK to Raspbery Pi GPIO 18<br />
Amp LRCLK to Raspbery Pi GPIO 19<br />
Run the following commands to setup:
```
sudo apt install -y wget
wget https://github.com/adafruit/Raspberry-Pi-Installer-Scripts/raw/main/i2samp.py
sudo -E env PATH=$PATH python3 i2samp.py
```
Reboot once install complete
If it sounds really distorted, it could be the volume is too high. However, in order to have volume control appear in Raspbian desktop or Retropie you must reboot a second time after doing the speaker test, with sudo reboot.Once rebooted, try running alsamixer and use arrow keys to lower the volume, 50% is a good place to start.

Use this command to test the speaker,it should generate white noise:
```
speaker-test -c2
```
Try to play an audio file with this command:
```
speaker-test -c2 --test=wav -w /usr/share/sounds/alsa/Front_Center.wav
```

Ensure that all the audio files required for the project are working:
```
./play_all_wav.sh
```
This will play all the audio needed for this project in order

Run the following command to start the overall program:
```
python controller.py
```
Press the button to start program<br />
All the scripts can be found above