from random import choice
from time import sleep, time
import RPi.GPIO as GPIO
import numpy
# from draft_full_1 import 

microstepping_dict = {"fullstep" : [0, 0, 0], "1/2": [1, 0, 0], "1/4": [0, 1, 0],
"1/8": [0, 0, 1], "1/16": [1, 1, 0], "1/32": [1, 1, 1] }  
Pins_dict = {"modes 1": [10, 12, 14], "modes 2": [15, 16, 17], "dir 1": 18, "dir 2": 20, "step 1": 21, 
"step 2": 25}

def pin_numbering_checker():
    """ Run this to ask user to confirm correct pin set up """
    print(Pins_dict)
    print("Is this the right pin set up? Type 'yes' or 'no' (note, changes made through console last time will not be saved)")
    input1 = input()
    if input1 == "yes":
        print("Sounds good, continuing.")
        return
    else:
        while True:
            print("Which one do you want to edit?")
            choice_of_edit = input()
         
            if choice_of_edit == "modes 1" or "modes 2":
                print("Which pins do you want to change? (0, 1, 2?)")
                choice_of_mode_pins1 = int(input())
                print("Choose the new pin for mode {} pin in {}".format(choice_of_mode_pins1, choice_of_edit))
                Pins_dict[choice_of_edit][choice_of_mode_pins1] = input()

            else:
                print("Choose the new pin for {}".format(choice_of_mode_pins1))
                Pins_dict[choice_of_edit] = input()
            
            print(Pins_dict)
            print("Would you like to continue editing the dictionary? (y or n)") 
            continue_editing = input()
            if continue_editing == "n":
                break

def setup_pins(pins, output_or_input):
    for pin in pins:
        if output_or_input == "output":
            GPIO.setup(pin, GPIO.OUTPUT, initial=GPIO.LOW)
        else:
            GPIO.setup(pin, GPIO.INPUT)

def rotation_full_step(number_rotations, dir, which_motor_step, frequency, dutycycle):
    dc = dutycycle
    degrees_per_pulse = 0.9
    pwm_object = GPIO.PWM(which_motor_step, frequency)
    pwm_object.start(dc)
    time_on = (number_rotations/degrees_per_pulse)/frequency
    sleep(time_on)
    pwm_object.stop()
    print("Moved by %s" % number_rotations)
    
def rotation_semi_step(number_rotations, dir, which_motor_step, frequency, dutycycle, microstep_type):   
    """
    make sure MODE_PINS are setup before running this function. 
    insert how to format input in here, and description of the function.
    """
    if microstep_type == "1":
        Pins_dict["modes 1"][0]
        """Fix/continue editing this condition"""
    degrees_per_pulse = 0.9
    pwm_object = GPIO.PWM(which_motor_step, frequency)
    pwm_object.start(dutycycle)
    time_on = (number_rotations/degrees_per_pulse)/frequency
    sleep(time_on)
    pwm_object.stop()
    print("Moved by %s" % number_rotations)

pin_numbering_checker