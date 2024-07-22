import sys
import speech_recognition as sr
from gpiozero import LED
import time
import threading
import subprocess


r = sr.Recognizer()
mic = sr.Microphone()

subprocess.call("sudo python alarm.py",shell=True)
print("Start talking")

while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)
    with open ("output.txt", "w") as file:
        file.write(words)
        sys.exit()
