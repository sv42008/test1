"""Controlling the motor from instructions set up from before."""

from time import sleep
# from RPi.GPIO import GPIO
from pi_pin_setup import *

# global variables to update in functions.
timer = 0
gbl_theta = 0
gbl_phi = 0
completion1 = False
error_angle_1 = 0
error_angle_2 = 0
# nbr_motor_1_angle = 0.0
# nbr_motor_2_angle = 0.0
# microstepping = microstepping_dict["1/2"]


def convert_string_to_float(which_string):
    # use an array with the second column to refer to the integer to which you want 
    # to convert to
    if which_string == "fullstep":
        which_string = 1.0
    elif which_string == "1/2":
        which_string = 0.5
    elif which_string == "1/4":
        which_string = 0.25
    elif which_string == "1/8":
        which_string = 0.125
    elif which_string == "1/16":
        which_string = 0.0625
    elif which_string == "1/32":
        which_string = 0.03125
    return which_string

def motion_parameters(delta_t, microstep1_str = "fullstep", microstep2_str = "fullstep"):
    """setup parameters for the motion of the motors, and setting up the microstepping"""
    
    #converting string into float 
    global microstep1, microstep2
    microstep1 = convert_string_to_float(microstep1_str)
    microstep2 = convert_string_to_float(microstep2_str)
    
    #setting up parameters as global variables 
    global del_t
    del_t = delta_t

    # setting up mode pins according to chosen microstepping
    for l in [microstep1_str, microstep2_str]:
        for i in range(3):
            if microstepping_dict[l][i] == 0:
                # set low
                print("{} set to low".format(pins_dict["modes 1"][i]))
                # GPIO.output(pins_dict["modes 1"][i], 0)
            elif microstepping_dict[l][i] == 1:
                # set high
                print("{} set to high".format(pins_dict["modes 1"][i]))
                # GPIO.output(pins_dict["modes 1"][i], 1)
            
    print("Parameters set: time interval = {}, microstepping for motor 1 = {}, microstepping for motor 2 = {}".format(delta_t, microstepping1, microstepping2))
    return

def epoch():
  # move and track progressing a unit of time
  sleep(del_t)
  global timer
  timer = timer + del_t
  print(timer)

def motor1_movements(theta):
    """moves the first motor by theta, and adds it to a current angle reading."""
    global completion1; completion1 = False

    STEP = pins_dict["step 1"]
    number_of_steps_unrounded = theta/(microstep1*0.9)
    number_of_steps = round(number_of_steps_unrounded)

    # updates the total error variables from rounding
    global error_angle_1; error_angle_1 = error_angle_1 + (number_of_steps_unrounded - number_of_steps)

    # pulse
    for i in range(number_of_steps):
        # GPIO.output(STEP, 1)
        print("pulse on")
        epoch()
        # GPIO.output(STEP, 0)
        print("pulse off")
        epoch()

    # updating current angle
    global gbl_theta
    gbl_theta = gbl_theta + theta
    print("current angle is {}".format(gbl_theta))

    # when code finishes running, update completion1 True.
    completion1 = True

    return 

def motor2_movements(phi):
    """moves the first motor by theta, and adds it to a current angle reading."""
    global completion2; completion2 = False

    STEP = pins_dict["step 2"]
    number_of_steps_unrounded = phi/(microstep2*0.9)
    number_of_steps = round(number_of_steps_unrounded)

    # updates the total error variables from rounding
    global error_angle_2; error_angle_2 = error_angle_2 + (number_of_steps_unrounded - number_of_steps)

    # pulse
    for i in range(number_of_steps):
        # GPIO.output(STEP, 1)
        print("pulse on")
        epoch()
        # GPIO.output(STEP, 0)
        print("pulse off")
        epoch()

    # updating current angle
    global gbl_phi
    gbl_phi = gbl_phi + phi
    print("current angle is {}".format(gbl_phi))

    # when code finishes running, update completion1 True.
    completion2 = True

    return 

def motors(theta_list, phi_list):
  for theta in theta_list:
        for phi in phi_list:
            epoch()
            motor1_movements(theta); motor2_movements(phi)
            epoch()
            

# testing code::

# motion_parameters(0.005, "1/2")

# print("current microstep chosen is {}".format(microstep1))
# motor1_movements(2)
# epoch()
# motor1_movements(3)