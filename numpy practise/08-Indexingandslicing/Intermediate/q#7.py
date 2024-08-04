# Write a NumPy program that creates a 3D NumPy array and use boolean indexing
# to select elements along one axis based on conditions applied to another axis.

import numpy as np

arr = np.array([[[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]]])

var1 = arr > 5

var2 = arr[var1]

print(var2)





