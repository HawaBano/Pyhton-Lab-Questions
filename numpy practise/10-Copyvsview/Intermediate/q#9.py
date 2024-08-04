# Create a numpy array and make a copy. Show that changing the shape of the
# copy does not affect the original array.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

var = arr.copy()
r_var = var.reshape((1, 9))

print("Original array:")
print(arr)

print("\nReshaped copy:")
print(r_var)
