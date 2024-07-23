import sys
import speech_recognition as sr
from gpiozero import LED
import time
import threading
import subprocess


r = sr.Recognizer()
mic = sr.Microphone()



while True:
    print("Start talking")
    with mic as source:
        subprocess.call("python3 ~/Adafruit_Python_SSD1306/examples/Talking.py",shell=True)
        subprocess.call("sudo python alarm.py",shell=True)
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)
    subprocess.call(['python',"Adafruit_Python_SSD1306/examples/Display.py","Processing"])
    with open ("output.txt", "w") as file:
        file.write(words)
        sys.exit()
