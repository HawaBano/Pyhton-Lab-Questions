# Convert a 1D numpy array of 16 elements to a 2D array of shape (4, 4).
import numpy as np

arr = np.arange(16)
var = arr.reshape(4,4)
print(var)