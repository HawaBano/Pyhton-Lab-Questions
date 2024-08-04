# Insert a new dimension into a 1D numpy array.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])

var = arr.reshape(1, -1)

print("Original 1D array:")
print(arr)
print("2D column:\n")
print(var)

