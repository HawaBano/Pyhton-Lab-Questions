# Write a NumPy program that creates a 3D NumPy array and uses  fancy indexing to
# select elements from specific rows and columns.

import numpy as np
arr = np.array([[[1,2,3],[4,5,6]]])
print(arr)
print(arr[[0, 1], [1, 1]])

