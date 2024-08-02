# Create a numpy array with a specified data type (int16).

import numpy as np

arr = np.array([1.2,4.6,4.5])
print(arr)
print(arr.dtype)


arr = np.array([1.2,4.6,4.5], dtype="int16")
print(arr)
print(arr.dtype)