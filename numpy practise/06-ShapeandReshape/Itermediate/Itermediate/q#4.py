# Reshape a 1D numpy array of 12 elements to a 3D array of shape (2, 2, 3).


import numpy as np

arr = np.arange(12)
var = arr.reshape(2, 2, 3)
print(var)