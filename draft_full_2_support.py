import numpy as np

def circle(radius):
    """lambda function returned for a circle with a certain radius"""
    return lambda x: (radius**2 - x**2)**(1/2)

def circle2(number_x, number_angle):
    """function which returns a [circle object] (need to figure this out)
    which takes a number_x and number_angle argument. """