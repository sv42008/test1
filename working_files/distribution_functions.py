import numpy as np
"""Contains functions for different distributions to put into a cartesian array"""
    
def circle_filled(arr, radius):
    width = arr.shape[1]
    height = arr.shape[0]
    for x in np.linspace(-1*(width/2), width/2, width+1):
        for y in np.linspace(height/2, -1*height/2, height+1):
            x_cood = int(x + width/2)
            y_cood = int(-1*(y + height/2))
            if x**2+y**2 <= radius**2:
                arr[int(y_cood)][int(x_cood)] = 1
    return arr
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
def circle_line(arr, radius, linewidth):
    width = arr.shape[1]
    height = arr.shape[0]
    for x in np.linspace(-1*(width/2), width/2, width+1):
        for y in np.linspace(height/2, -1*height/2, height+1):
            x_cood = int(x + width/2)
            y_cood = int(-1*(y + height/2))
            if x**2+y**2 >= radius**2-(linewidth/2)**2 and x**2+y**2 <= radius**2+(linewidth/2)**2:
                arr[int(y_cood)][int(x_cood)] = 1
    return arr

def all_filled(arr):
    width = arr.shape[1]
    height = arr.shape[0]
    all_coordinates = np.argwhere(arr == 0)
    for i in all_coordinates:
        arr[i[0]][i[1]] = 1
    return arr