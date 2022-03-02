import numpy as np
import distribution_functions

def new_array():
    """create an array with rows = theta, columns = x
    can generalise the size of the array later."""
    return np.zeros((1000, 1000))


def putting_a_distribution_into_array(real_space_array, distribution_function):
    width_arr = real_space_array.shape[1]
    height_arr = real_space_array.shape[0]
    for i in range(width_arr):
        for j in range(height_arr):
            real_space_array[i][j] = 1