from time import sleep
from draft_full_1 import initialise_GPIO

import initialise_motor as im
import RPi.GPIO as GPIO
import numpy as np
from polar_coordinate_array_generator import *
from stepper_motor_control1 import Pins_dict

def quick_circle(filled_polar_array):
    """[fixxx ] Specific function for printing circles,"""
    for i in filled_polar_array.shape[0]:
        if filled_polar_array[i] != 0:
            for ii in filled_polar_array[i]:
                return
            return
        return
    pass

def quick_circle(array_with_circle):
    """Call after initialisation of pins"""
    frequency = 100 
    # will need to find a solution as to how to design frequency.
    for i in array_with_circle.shape[1]:
        if array_with_circle[i, :] == 1:
            a = GPIO.PWM(Pins_dict["step 1"][0], frequency)
            a.start()
        

# initialises all mode pins as output
# put this into the intialisation .py file.
im.setup_pins(Pins_dict["modes 1"])
im.setup_pins(Pins_dict["modes 2"])
im.setup_pins(Pins_dict["step 1"])
im.setup_pins(Pins_dict["step 2"])
im.setup_pins(Pins_dict["dir 1"])
im.setup_pins(Pins_dict["dir 2"])

