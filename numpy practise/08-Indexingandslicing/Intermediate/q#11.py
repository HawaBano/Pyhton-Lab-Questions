# Write a NumPy program that creates a 3D NumPy array and uses integer array indexing to
# select elements along specific axes.

import numpy as np

array = np.array([[[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]])
var = array[0:1, 1:1,1:2]
print(var)