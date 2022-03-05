from array_creator import *
from distribution_functions import *
from array_conversion import *

# Initialising array
resolution_of_arr(20)
polar_zeros_arr = polar_zeros()
cart_zeros_arr = cartesian_zeros()

# Circle line into cartesian array:
cart_arr = circle_line(cart_zeros_arr, 5, 7)

# Convert into polar array:
polar_arr = cartesian_to_polar(cart_arr, polar_zeros_arr)

print(polar_arr)
print(cart_arr)