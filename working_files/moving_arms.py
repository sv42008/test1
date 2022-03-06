"""code which 1. defines the arm lengths in mm, 2. converts a polar array into an output of"""

# import RPi.GPIO as GPIO
import numpy as np

# arm lengths in mm
# we need the second arm to be the same length to not produce deadspace.
# code does not currently account for deadspace.  
first_arm_length = 10
second_arm_length = 10 
b = second_arm_length/first_arm_length

def first_arm_angle(r):
    """returns positive theta, not rotated"""
    r_tilda = r/first_arm_length
    cos_theta = (-1*b**2 + r_tilda**2 + 1)/(2*r_tilda)
    return np.arccos(cos_theta)

def second_arm_angle(r):
    """Returns clockwise positive phi angle, not rotated"""
    r_tilda = r/first_arm_length
    cos_phi = (b**2 + r_tilda**2 - 1)/(2*b*r_tilda)
    phi = 2*np.pi - np.arccos(cos_phi) 
    return phi

def reading_polar_arr(arr):
    """returns array of first column = theta, second column = phi"""
    non_zero_coordinates = np.argwhere(arr)
    angle_arr =np.zeros((1, 2))
    for i in non_zero_coordinates:
        r = i[1]
        chi = i[0]
        if r == 0:
            phi = (3/2)*np.pi 
            theta_prime = np.pi/2
        else:
            phi = second_arm_angle(r)
            theta_prime = first_arm_angle(r)
        # print(r, " ", phi, " ", theta_prime)
        theta = theta_prime + chi
        print([phi, theta])
        np.append(angle_arr, np.array([theta, phi]), axis = 0)

        # print(angle_arr)
    return angle_arr

        
array_random = np.zeros((10, 10))
for i in range(10):
    array_random[np.random.randint(10)][np.random.randint(10)] =1
print(reading_polar_arr(array_random))