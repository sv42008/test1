from time import sleep

from matplotlib.pyplot import fill
from pandas import array
import RPi.GPIO as GPIO
import numpy as np
from polar_coordinate_array_generator import *

def quick_circle(filled_polar_array):
    """[fixxx ] Specific function for printing circles,"""
    for i in filled_polar_array.shape[0]:
        if filled_polar_array[i] != 0:
            for ii in filled_polar_array[i]:
                return
            return
        return
    pass

def quick_circle(array_with_circle):
    for i in array_with_circle.shape[0]:
        if array_with_circle[i, :] == 1:


