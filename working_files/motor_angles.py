"""code which 1. defines the arm lengths in mm, 2. converts a polar array
 into an output of two lists, theta and phi."""

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
    """returns two lists, first theta, second phi"""
    non_zero_coordinates = np.argwhere(arr)
    theta_list = []
    phi_list = []
    for i in non_zero_coordinates:
        r = i[1]
        chi = i[0]
        if r == 0:
            phi = (3/2)*np.pi 
            theta_prime = np.pi/2
        else:
            phi = second_arm_angle(r)
            theta_prime = first_arm_angle(r)

        theta = theta_prime + chi
        theta_list.append(theta)
        phi_list.append(phi)
       
    return theta_list, phi_list