""" Code for robot to output distributions fed in to a robot.

# We are using software timing (Packages like time and RPi.GPIO) which means interrupts in the Linux Kernal can 
# lead to delays and changes in timing. 

# We want this program to function as an "interface" which we can feed a distribution
# and then move the robot to recreate that distribution to scale.

# This will depend on what our robot looks like. 
"""
from time import sleep
#import RPi.GPIO as GPIO
import numpy

# GLOBAL VARIABLES:

# CLASS DEFINITIONS:

# # superclass petridish can have subclasses of circle, or rectangle, or other we can add.
class petridish():
    """ _title = name for dish, density = distance between drops in m, 
    # scale = tuple, for circle = radius, for rectangle = height and width, 
    # volume = volume of droplet """
       
    def __init__(self, _title, density, scale, volume): 
        self.name = _title
        self.density = density
        self.scale = scale
        self.volume = volume
    
    def print_details(self):
        print(f'Name = {self.name}')
        print(f'Density = {self.density}')
        print(f'Scale = {self.scale}')
        print(f'Volume = {self.volume}')
    
    
class circular_dish(petridish):
    def set_scale(self, scale): # scale is a tuple, with radius in m
        self.radius = scale[0]

class rectangular_dish(petridish):
    def set_scale(self, scale): # scale is a tuple, with width as (0) and height of (1)
        self.width = scale[0]
        self.height = scale[1]
                

# FUNCTIONS:

def initialise_GPIO(self, list_of_pins):
   
    GPIO.setmode(GPIO.BCM) # setting the board numbering to Broadcom
    for pin in list_of_pins: # loop to set listed pins to output mode
        if pin in (27, 22, 11, 21):
            print("Broken pins chosen. Please choose other GPIO pins. Also, double check the numbering system being used (this code uses Broadcom)")
            return
        GPIO.setup(pin, GPIO.OUT)


def initialise_petridish(name, shape, separation, scale, volume):
    """set this equal to an object, which will be a tuple, with the first being an 
    array and the second an object of 'petridish' class as defined above."""
    if shape == 'circle':
        circle_object = circular_dish(name, separation, scale, volume)
        total_array_circle = numpy.zeros((2*scale[0], 2*scale[0]))
        return total_array_circle, circle_object

    elif shape == 'rectangle':
        rectangle_object = rectangular_dish(name, separation, scale, volume)
        total_array_rectangle = numpy.zeros((scale[0],scale[1]))
        return total_array_rectangle, rectangle_object
    
    else:
        print('Incorrect shape provided, please write either \'circle\' or \'rectangle\', with no spaces.')

#   Distribution functions:
 
straightline =  lambda x, gradient: gradient*x # = y
circle_not_filled = lambda x, radius: (radius**2 - x**2)**(1/2) # = y

#   functions to install the distributions:

def distribution_into_matrix(tuple_with_array_and_object, distribution_lambda_function = straightline, *args):
    """ tuple_with_ar... is returned from the initialise_petridish function
    this function returns a modified zeros array with 'ones (1s)' as per the function we are feeding in.
    The function defaults to the line function.
    for *args, put in arguments that the chosen distribution function requires, in correct order, !!EXCEPT FOR X!!.
    """
    total_array = tuple_with_array_and_object[0]
    petridish_object = tuple_with_array_and_object[1]
    x_axis_length = total_array.shape[0]
    for x in range(x_axis_length): # i.e. along the x-axis, place a 1 in the along the y-axis according to function.
        print(x)
        dlf = distribution_lambda_function(x, args[0])
        #if dlf.is_complex:
           # total_array[x, ]
        if dlf.real < x_axis_length: # condition to ensure that we account for the case where we exceed size of array 
            total_array[x, int(dlf.real) - int((x_axis_length/2))] = 1 
        else:
            pass

    # print (total_array)

    return total_array

def circle_distribution_into_matrix(tuple_with_array_and_object, distribution_lambda_function = straightline, *args):
    """ tuple_with_ar... is returned from the initialise_petridish function
    this function returns a modified zeros array with 'ones (1s)' as per the function we are feeding in.
    The function defaults to the line function.
    for *args, put in arguments that the chosen distribution function requires, in correct order, !!EXCEPT FOR X!!.
    """
    total_array = tuple_with_array_and_object[0]
    petridish_object = tuple_with_array_and_object[1]
    x_axis_length = total_array.shape[0]
    y_axis_length = total_array.shape[1]
    radius_squared = int(args[0]**2)
    line_width = 3
    for x in range(x_axis_length):
        for y in range(y_axis_length):
            circle_test_value = int((x - (x_axis_length/2))**2 + (y-(y_axis_length/2))**2)
            if circle_test_value > radius_squared - line_width and circle_test_value < radius_squared + line_width :
                total_array[x, y] = 1
            else:
                total_array[x, y] = 0
    
    # print (total_array)

    return total_array
    

# print(distribution_into_matrix(initialise_petridish('first', 'circle', 1, (10, 10), 1), straightline, 2))

# print(distribution_into_matrix(initialise_petridish('first', 'circle', 1, (10, 10), 1), circle_not_filled, 3))

a = circle_distribution_into_matrix(initialise_petridish('first', 'circle', 1, (10, 10), 1), circle_not_filled, 5)

print(a)