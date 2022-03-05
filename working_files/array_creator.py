import numpy as np
"""Creates empty arrays, either polar or cartesian, for a set interval spacing. 
Run the resolution_of_arr before creating the empty array"""

def resolution_of_arr(number_intervals):
    """If I am to keep the save number of intervals, I don't need so many different 
    variables. But this will be good to allow for changes in size of array."""
    global no_steps_in_r, no_steps_in_y, no_steps_in_x, no_steps_in_theta
    
    no_steps_in_r = number_intervals; print("No. in r: ", no_steps_in_r)
    no_steps_in_theta = number_intervals; print("No. in theta: ", no_steps_in_theta)
    no_steps_in_x = number_intervals; print("No. steps in x: ", no_steps_in_x)
    no_steps_in_y = number_intervals; print("No. steps in y: ", no_steps_in_y)

def polar_zeros():
    return np.zeros((no_steps_in_r, no_steps_in_theta))

def cartesian_zeros():
    return np.zeros((no_steps_in_x, no_steps_in_y))