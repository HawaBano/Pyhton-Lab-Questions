# Create a numpy array with values ranging from 0 to 2 with a step size of 0.3.

import numpy as np
arr = np.arange(0, 2,0.3, )
print(arr)

# Default parameter
# def add_numbers(a = 30, device=None):
#     print("Value of a", a)
#     print("Value of b", b)
#     return a + b
#
# add_numbers(40)

#Named Parameter

def add_numbers(a = 30, b=20):
    print("Value of a", a)
    print("Value of b", b)
    return a + b



add_numbers(b = 40)
add_numbers(20)
add_numbers(20, 30)

