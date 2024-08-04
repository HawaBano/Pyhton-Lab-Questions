# Perform element-wise subtraction of a 2D array of shape (3, 3) with a 1D
# array of shape (3,).

import numpy as np

arr = np.array([[1,2,3],[4, 5, 6],[7, 8, 9]])

arr2 = np.array([1,2,3])

var = arr - arr2
print(var)