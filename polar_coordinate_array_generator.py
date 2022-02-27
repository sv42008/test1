import numpy as np
"""Function which returns an array with r along the x axis of array, and the angle along
the y axis. Can generalise by using rotational symmetry in our system."""

def array_creator(number_x, number_angle):
    return np.zeros((number_x, number_angle))

def circle_creator(radius, zeros_array):
    """returns modified array with 1s along a certain radius"""
    zeros_array[:, [radius-1]] = 1
    return zeros_array

def circle_thickness(radius, thickness, zeros_array):
    zeros_array[:, (radius-1)-int(round(thickness/2, 0)): (radius-1) + int(round(thickness/2, 0))] =1
    return zeros_array 