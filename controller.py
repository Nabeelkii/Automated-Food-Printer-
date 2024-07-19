import time
import os
import signal
import subprocess
from gpiozero import Button, LED

# Pin definitions
tactile_switch = Button(25)  # GPIO pin 36
Green_LED = LED(26)  # GPIO pin 11

# Paths to the scripts you want to run
shell_script_path = './master.sh'  # Shell script path

# Global variables for processes and state
shell_process = None  # Global variable definition for the shell script

led_on = False  # State to track if the LED and scripts are on

# Function to start running all scripts
def start_scripts():
    global shell_process, python_process
    
    shell_process = subprocess.Popen(['bash', shell_script_path])  # Start the shell script
    print(f"Started shell script with PID {shell_process.pid}")

# Function to terminate all scripts 
def terminate_scripts():
    global shell_process, python_process
    if shell_process:
        os.kill(shell_process.pid, signal.SIGTERM)

        #shell_process.terminate()  # Kill the Shell script
        #shell_process.wait()

# Function to turn on LED and run all scripts
def turn_on_green_led():
    global led_on
    if not led_on:
        Green_LED.on()  # Turn on LED
        start_scripts()  # Start up the scripts
        led_on = True
        print("Green LED turned on")

# Function to turn off LED and terminate all scripts
def turn_off_green_led():
    global led_on
    if led_on:
        Green_LED.off()  # Turn off LED
        terminate_scripts()  # Shut down the scripts
        led_on = False
        print("Green LED turned off")

# Function to toggle LED and scripts state
def toggle_green_led():
    global led_on
    if led_on:
        Green_LED.off()  # Turn off LED
        terminate_scripts()  # Shut down the scripts
        led_on = False
        print("Green LED turned off")
    else:
        Green_LED.blink(on_time=1, off_time=1)  # Blink LED
        start_scripts()  # Start up the scripts
        led_on = True
        print("Green LED blinking")

# Function that handles button press
def handle_button():
    global led_on
    press_time = time.time()
    while tactile_switch.is_pressed:
        if time.time() - press_time > 3:  # Held for more than 3 seconds
            return
        time.sleep(0.1)
    toggle_green_led()

# Set up event handlers for button press and release
def button_pressed():
    handle_button()

# Attach event handlers
tactile_switch.when_pressed = button_pressed

try:
    while True:
        time.sleep(0.1)  # Polling interval
except KeyboardInterrupt:
    terminate_scripts()
    print("Main script exiting...")
