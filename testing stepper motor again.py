# Testing stepper motor again; using other motor driver

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
list_of_pins = (20, 16, 12, 7)
GPIO.setup(list_of_pins, GPIO.OUT)

# Simple PWM generation
def flashing(frequency):
    dutycycle = 50

    p = GPIO.PWM(20, frequency)
    p.start(dutycycle)
    input('Press return to stop ')
    p.stop()

flashing(15)