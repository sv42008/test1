import numpy as np

def cartesian_to_polar(cartesian_array):
    non_zero_coordinates = np.argwhere(cartesian_array == 1)
    x = []; y = []; chi = []
    for i in range(non_zero_coordinates.shape[0]):
        x.append(non_zero_coordinates[i, 0])
        y.append(non_zero_coordinates[i, 1])
    
    no_steps_in_one_degree = 1
    steps_along_r = 15
    number_of_angle_steps = 15
    # number_of_angle_steps = 360*no_steps_in_one_degree
    polar_arr = np.zeros((number_of_angle_steps, steps_along_r))

    for i in range(len(x)):
        if x[i] == 0:
            if y[i]<=0:
              chi.append(-np.pi/2)
            else:
              chi.append(np.pi/2)
        else:
            chi.append(np.arctan(y[i]/x[i]))
    for j in chi:
        print(j)

    return polar_arr