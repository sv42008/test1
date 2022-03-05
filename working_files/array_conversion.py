import numpy as np
"""Function to convert cartesian distribution in array into polar array."""

def cartesian_to_polar(cartesian_arr, polar_arr):
  width = cartesian_arr.shape[1]
  height = cartesian_arr.shape[0]
  drop_coordinates = np.argwhere(cartesian_arr == 1)
  
  # r length to cartesian coordinate:
  centre_point = [int(height/2), int(width/2)]
  for i in drop_coordinates:  
      x_distance = i[1] - centre_point[1]
      y_distance = i[0] - centre_point[0]
      r = (x_distance**2 + y_distance**2)**(1/2)
      angle = np.arctan(y_distance/x_distance)

      if x_distance >= 0 and y_distance >= 0:
        chi = angle
      elif x_distance < 0 and y_distance >= 0:
        chi = np.pi + angle
      elif x_distance < 0 and y_distance < 0:
        chi = np.pi + angle
      elif x_distance >= 0 and y_distance < 0:
        chi = 2*np.pi + angle

      polar_arr[int((chi/(2*np.pi))*height)][int(r)] = 1

  return polar_arr