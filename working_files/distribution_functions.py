# from cmath import polar
from matplotlib.pyplot import polar
import numpy as np

def cartesian_to_polar(array1):
    non_zero_coordinates = np.argwhere(array1 == 1)
    x = []
    y = []
    for i in range(non_zero_coordinates.shape[0]):
        x.append(non_zero_coordinates[i, 0])
        y.append(non_zero_coordinates[i, 1])
    r  = (x**2 + y**2)**(1/2)
    
    chi = []
    for i in range(len(x)):
        if x[i] == 0:
            chi.append(np.pi/2)
        else:
            c = y[i]/x[i]
            chi.append(np.arctan(c))
    # want to return polar coordinate array
    polar_zeros_arr = np.zeros((non_zero_coordinates.shape[0], non_zero_coordinates[1]))
    for i in chi:
        for j in r:
            polar_zeros_arr[i, j] = 1
    polar_arr = polar_zeros_arr
    return polar_arr

def circle_into_array(general_array):
    """this function places a circle in a general array fed in."""
    height_array = general_array.shape[0]
    width_array = general_array.shape[1]
    
def circle_lambda_fn():
    return lambda x, radius: (radius**2 - x**2)**(1/2) # = y

def straight_line_lambda_fn():
    return lambda x, gradient: gradient*x # = y

def circle_distrn_2(radius):
    return radius**2




    
