# Convert a numpy array of floats to integers.


import numpy as np

arr = np.array([1.2,4.6,4.5])
print(arr)
print(arr.dtype)


arr = np.array([1.2,4.6,4.5],dtype="i")
print(arr)
print(arr.dtype)



