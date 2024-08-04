# Use np.copy to make a deep copy of a numpy array and verify changes to the
# copy do not affect the original.


import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
var = np.copy(arr)
var[0] = 99
print("Modified copied array:", var)
print("Original array after modification of copy:", arr)
