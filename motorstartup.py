from gpiozero import DigitalOutputDevice
from time import sleep
import sys
# Define the L298N connections
IN1 = DigitalOutputDevice(17)  # GPIO pin 17
IN2 = DigitalOutputDevice(27)  # GPIO pin 18
IN3 = DigitalOutputDevice(22)  # GPIO pin 27
IN4 = DigitalOutputDevice(23)  # GPIO pin 22
ENA = DigitalOutputDevice(6)  # GPIO pin 23 for ENA
ENB = DigitalOutputDevice(13)  # GPIO pin 24 for ENB

# Set ENA and ENB to high to enable the motor channels
ENA.on()
ENB.on()

sys.exit()

# Steps per revolution for your stepper motor
steps_per_revolution = 200
delay = 0.01  # Adjust delay to control speed

def step_sequence(step):
    seq = [
        (1, 0, 0, 1),
        (1, 0, 0, 0),
        (1, 1, 0, 0),
        (0, 1, 0, 0),
        (0, 1, 1, 0),
        (0, 0, 1, 0),
        (0, 0, 1, 1),
        (0, 0, 0, 1)
    ]
    IN1.value = seq[step][0]
    IN2.value = seq[step][1]
    IN3.value = seq[step][2]
    IN4.value = seq[step][3]

def stepper_motor(steps, direction):
    for _ in range(steps):
        for step in range(8):
            if direction == 1:
                step_sequence(step)
            else:
                step_sequence(7 - step)
            sleep(delay)

try:
    while True:
        # Rotate clockwise
        #stepper_motor(steps_per_revolution, 1)
        sleep(1)
        
        # Rotate anticlockwise
        #stepper_motor(steps_per_revolution, -1)
        sleep(1)
except KeyboardInterrupt:
    print("Program stopped")
