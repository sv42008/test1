from main import *

# this script will run the functions to test the motor arrangement.
for i in pins_dict:
    setup_pins(pins_dict[i])

def resolution_of_array_testing():
    for i in np.linspace(10, 100, 10):
        ii = int(i)
        resolution_of_arr(ii)
        polar_zeros_arr = polar_zeros()
        cart_zeros_arr = cartesian_zeros()

        cart_arr = circle_line(cart_zeros_arr, ii/10, 7)
        polar_arr =  cartesian_to_polar(cart_arr, polar_zeros_arr)
        
        angles = reading_polar_arr(polar_arr)
        theta_list = angles[0]
        phi_list = angles[1]

motion_parameters(0.1)
