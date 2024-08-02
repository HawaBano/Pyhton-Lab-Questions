# Create a numpy array of floats and convert it to a numpy array of complex numbers.


import numpy as np

arr = np.array([2.3,4.5,5.7])
print(arr)
print(arr.dtype)

var = arr.astype(complex)
print(var)
print(var.dtype)