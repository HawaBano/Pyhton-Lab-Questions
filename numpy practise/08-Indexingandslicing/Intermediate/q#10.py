# Write a NumPy program that creates a 2D NumPy array and uses boolean indexing to replace all elements
# that meet a certain condition with a specified value

import numpy as np

arr = np.array([[1, 2, 3, 4, 5, 6]])

var = arr>5
var2 = arr[var,[10, 11, 12, 13]]
print(var2)