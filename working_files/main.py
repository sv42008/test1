"""Main Python file calling the rest of the python .py files in the folder."""

from array_creator import *
from distribution_functions import *
from array_conversion import *
from motor_angles import *
from pi_pin_setup import *
from motor_pump_control import *

# Initialising array
resolution_of_arr(20)
polar_zeros_arr = polar_zeros()
cart_zeros_arr = cartesian_zeros()

# Circle line into cartesian array:
cart_arr = circle_line(cart_zeros_arr, 5, 7)

# Convert into polar array:
polar_arr = cartesian_to_polar(cart_arr, polar_zeros_arr)

# Getting angles from 
angles = reading_polar_arr(polar_arr)
theta_list = angles[0]
phi_list = angles[1]

# check pins
pin_numbering_checker()
broken_pin_checker()

# setup pins to output/input
for i in pins_dict:
    #  setting all pins in pins_dict (modes, dir, step) to output
    setup_pins(pins_dict[i])

#running motor
motion_parameters(0.005, "fullstep")
motors(theta_list, phi_list)