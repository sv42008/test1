"""Controlling the motor from instructions set up from before."""

from time import sleep
from RPi.GPIO import GPIO
from pi_pin_setup import *

# global variables to update in functions.
timer = 0
gbl_theta = 0
gbl_phi = 0
microstepping = microstepping_dict["1/2"]

def motion_parameters(delta_t, microstepping1 = "fullstep", microstepping2 = "fullstep"):
    """setup parameters for the motion of the motors, and setting up the microstepping"""

    #setting up parameters as global variables 
    global del_t; global microstep1; global microstep2
    microstep1 = microstepping1; microstep2 = microstepping2; del_t = delta_t
    microsp_list = []
    microsp_list.append(microstep1); microsp_list.append(microstep2)
    
    # setting the pins to 
    for l in microsp_list:
        print(l)
        for i in range(3):
            if microstepping_dict[l][i] == 0:
                # set low
                print("{} set to low".format(pins_dict["modes 1"][i]))
                # GPIO.output(pins_dict["modes 1"][i], 0)
            elif microstepping_dict[l][i] == 1:
                # set high
                print("{} set to high".format(pins_dict["modes 1"][i]))
                # GPIO.output(pins_dict["modes 1"][i], 1)
            
    print("Parameters set: time interval = {}, microstepping for motor 1 = {}, microstepping for motor 2 = {}".format(delta_t, microstep1, microstep2))
    return

def epoch():
  # move and track progressing a unit of time
  sleep(del_t)
  timer = timer + 1

def motor1_movements(angle):
    STEP = pins_dict["step"]
    no_movements = microstepping
    # STEP pin set high for delta_t
    GPIO.output(STEP, 1)

def motors(theta_list, phi_list):
  for theta in theta_list:
    for phi in phi_list:
      epoch()
      motor1_movements

motion_parameters(0.005, "1/2")