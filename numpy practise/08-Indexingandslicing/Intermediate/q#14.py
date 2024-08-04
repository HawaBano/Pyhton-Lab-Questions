#
# Write a NumPy program that creates a 2D NumPy array and uses slicing in
# combination with index arrays to select a rectangular subarray.
import numpy as np

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print(array)
print()
var = array[0:2, 1:4]

print(var)
