# Insert a value into a sorted 1D numpy array and keep it sorted.

import numpy as np
arr = np.array([1, 3, 5, 7, 9])
index = np.searchsorted(arr, 6)
var = np.insert(arr, index, 6)

print("Original array:", arr)
print("New array:", var)
