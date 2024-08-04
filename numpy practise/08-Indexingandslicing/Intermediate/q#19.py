# Write a NumPy program that creates a 5D NumPy array.
# Use boolean indexing to select elements along specific
# dimensions based on conditions applied to other dimensions.
import numpy as np

array = np.array([[[[[1, 2, 3, 4],
                     [5, 6, 7, 8]]]]])
print("Original Array:")
print(array)
var = array[array > 4]
print()
print(var)
