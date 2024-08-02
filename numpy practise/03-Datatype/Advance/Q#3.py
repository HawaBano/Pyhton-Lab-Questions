# Create a numpy array of shape (3, 3) with int8 data type and change it to int64.


import numpy as np

arr = np.ones((3,3),dtype= np.int8)
print(arr)
print(arr.dtype)

var = arr.astype(np.int64)
print(var)
print(var.dtype)