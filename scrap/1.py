
import numpy


class petridish():
    def __init__(self, name, density):
        self.name = name
        self.density = density
    
    def print_details(self):
        print(self.name)
        print(self.density)

circle1 = petridish('first_circle', 10)
circle1.print_details()

def lambda_function():
    return lambda x, a : x*a

print(lambda_function()(2,3))

class circular_dish(petridish):
    def set_scale(self, scale): # scale is a tuple, with radius in m
        self.radius = scale[0]

def function2():
    a = 2
    b = 3
    return a, b

print(function2()[0])

a = numpy.zeros((5,5))

straightline =  lambda x, b : b*x

def insert_into_array( x, b):
    for i in range(a.shape[0]):
        uu = straightline(x, b)
        a[i, uu] = 1
    return a

insert_into_array(3,1)
print(insert_into_array(3,1))

def insert_into_array2(lambda_function, *args):
    for i in range(a.shape[0]):
        uu = lambda_function(*args)
        a[i, uu] = 1
    return a

a2 = insert_into_array2(straightline, 3, 1)
print(a2)        