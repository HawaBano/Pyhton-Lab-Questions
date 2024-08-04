# Create a numpy array and create a view with np.asfortranarray.
# Modify the view and demonstrate the impact on the original array.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
var = np.asfortranarray(arr)

var[0, 0] = 10
var[1, 2] = 20
print(var)
print("\nOriginal array after modifying the view:")
print(arr)
