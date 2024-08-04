# Write a NumPy program that creates a 2D NumPy array and uses np.nonzero to
# find indices of elements that satisfy a condition, then uses these indices for advanced indexing

import numpy as np
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]])

print("Original Array:")
print(array)
var = np.nonzero(array > 50)
print(var)