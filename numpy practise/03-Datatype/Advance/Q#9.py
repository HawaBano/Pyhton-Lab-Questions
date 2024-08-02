# Create a numpy array with float64 and cast it to int32 without creating a new array.


import numpy as np


arr = np.array([1.5, 2.5, 3.5], dtype=np.float64)

arr.astype(np.int32, copy=False)

print(arr)
print(arr.dtype)