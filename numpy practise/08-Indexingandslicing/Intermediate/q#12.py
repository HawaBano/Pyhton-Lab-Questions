# Write a NumPy program that creates a 2D NumPy array and uses a combination of boolean
# and integer indexing to select a subset of elements.

import numpy as np

array = np.array([[10, 20, 30, 40],
                  [50, 60, 70, 80],
                  [90, 100, 110, 120]])
print(array)
arr = array > 50
var2 = array[arr]
print(var2)

