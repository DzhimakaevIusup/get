import time
import RPi.GPIO as GPIO
led = 26
GPIO.setmode(GPIO.BCM)
state = 0
GPIO.setup(led, GPIO.OUT)

button = 13
GPIO.setup(button, GPIO.IN)
while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)