# Add a 1D array [1, 2, 3] to each row of a 2D array of shape (3, 3).

import numpy as np

arr1 = np.array([[1, 2, 3],[1, 2, 3], [1, 2, 3]])
arr2 = np.array([1, 2, 3])

var = arr1 + arr2

print(var)

