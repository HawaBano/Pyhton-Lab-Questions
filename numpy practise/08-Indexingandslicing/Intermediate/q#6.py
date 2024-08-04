# Write a NumPy program that creates a 2D NumPy array and uses integer indexing with broadcasting
# to select elements from specific rows and all columns.

import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr)

var = arr[ [1, 2], :]
print()
print(var)
