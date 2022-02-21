from time import sleep, time
from turtle import circle
import RPi.GPIO as GPIO
import numpy
from draft_full_1 import 

microstepping_dict = {"fullstep" : [0, 0, 0], "1/2": [1, 0, 0], "1/4": [0, 1, 0],
"1/8": [0, 0, 1], "1/16": [1, 1, 0], "1/32": [1, 1, 1] }  
Pins_dict = {"Mode Pins 1": [10, 12, 14], "Mode Pins 2": [15, 16, 17], "Dir Pin 1": 18, "Dir Pin 2": 20, "Step pin 1": 21, 
"Step pin 2": 25}

def pin_numbering_checker():
    """ Incomplete, double check this later. """
    for pins in Pins_dict:
        print("MODE PIN 1 is %s", s = pins["Mode Pins 1"][1])
        input ("Press return to confirm, space to reject")

def setup_pins(pins, output_or_input):
    for pin in pins:
        if output_or_input == "output":
            GPIO.setup(pin, GPIO.OUTPUT, initial=GPIO.LOW)
        else:
            GPIO.setup(pin, GPIO.INPUT)

MODE_PINS_dict = [10, 12, 14]
setup_pins(MODE_PINS, "output")

def rotation_full_step(number_rotations, dir, which_motor_step, frequency, dutycycle):
    dc = dutycycle
    degrees_per_pulse = 0.9
    pwm_object = GPIO.PWM(which_motor_step, frequency)
    pwm_object.start(dc)
    time_on = (number_rotations/degrees_per_pulse)/frequency
    sleep(time_on)
    pwm_object.stop()
    print("Moved by %s" s=number_rotations)
    
def rotation_semi_step(number_rotations, dir, which_motor_step, frequency, dutycycle, microstep_type):   
    """
    make sure MODE_PINS are setup before running this function. 
    insert how to format input in here, and description of the function.
    """
    if microstep_type == "1":
        

    dc = dutycycle
    degrees_per_pulse = 0.9
    pwm_object = GPIO.PWM(which_motor_step, frequency)
    pwm_object.start(dc)
    time_on = (number_rotations/degrees_per_pulse)/frequency
    sleep(time_on)
    pwm_object.stop()
    print("Moved by %s" s=number_rotations)

