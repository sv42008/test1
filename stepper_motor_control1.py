from time import sleep, time
from turtle import circle
import RPi.GPIO as GPIO
import numpy
from draft_full_1 import 

def setup_pins(pins, output_or_input):
    for pin in pins:
        if output_or_input = output:
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
    print("Moved by %s" s=number_rotations)
    
def rotation_semi_step(number_rotations, dir, which_motor_step, frequency, dutycycle, microstep_type):
    if microstep_type == 1:
        setup_pins()
    dc = dutycycle
    degrees_per_pulse = 0.9
    pwm_object = GPIO.PWM(which_motor_step, frequency)
    pwm_object.start(dc)
    time_on = (number_rotations/degrees_per_pulse)/frequency
    sleep(time_on)
    pwm_object.stop()
    print("Moved by %s" s=number_rotations)

