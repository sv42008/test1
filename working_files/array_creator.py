import numpy as np
import distribution_functions

def resolution_of_arr(number_intervals):
    """If I am to keep the save number of intervals, I don't need so many different 
    variables. But this will be good to allow for changes in size of array."""
    global no_steps_in_r, no_steps_in_y, no_steps_in_x, no_steps_in_theta
    
    no_steps_in_r = number_intervals; print("No. in r: ", no_steps_in_r)
    no_steps_in_theta = number_intervals; print("No. in theta: ", no_steps_in_theta)
    no_steps_in_x = number_intervals; print("No. steps in x: ", no_steps_in_x)
    no_steps_in_y = number_intervals; print("No. steps in y: ", no_steps_in_y)

print(no_steps_in_r, " ", no_steps_in_theta)

def polar_zeros():
    return np.zeros((no_steps_in_r, no_steps_in_theta))

def cartesian_zeros():
    return np.zeros((no_steps_in_x, no_steps_in_y))

# def putting_a_distribution_into_array(arr, distribution_function):
#     width_arr = real_space_array.shape[1]
#     height_arr = real_space_array.shape[0]
#     for i in range(width_arr):
#         for j in range(height_arr):
#             real_space_array[i][j] = 1