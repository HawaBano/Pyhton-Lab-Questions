# Write a NumPy program that creates a 2D NumPy array and uses a mask array
# (boolean array) for indexing to select a subset of elements that match the mask criteria.

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr)
var = arr[arr > 30]
print()
print(var)
