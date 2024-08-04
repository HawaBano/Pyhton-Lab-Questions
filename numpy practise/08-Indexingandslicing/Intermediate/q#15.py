#Write a NumPy program that creates a 3D NumPy array and uses boolean
# indexing to set elements that meet a condition to a new value.

import numpy as np

arr = np.array([[[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]])
var = arr > 5
arr[var] = 99
print(arr)