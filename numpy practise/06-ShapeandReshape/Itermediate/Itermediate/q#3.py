# Flatten a 2D numpy array to a 1D array.

import numpy as np

arr = np.array([[1, 2 ,3 ,4 ,5 ],[6 ,7 ,8 ,9, 10]])
print(arr.ndim)
var = arr.flatten()
print(var)
print(var.ndim)