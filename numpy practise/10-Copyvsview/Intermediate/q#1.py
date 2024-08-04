# Create a numpy array and make a copy of it.
# Modify the copy and show that the original array remains unchanged.

import numpy as np

arr = np.array([1,2,3,4,5])

var = arr.copy()
var[3] = 9
print(arr)
print(var)