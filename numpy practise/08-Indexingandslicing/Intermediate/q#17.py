# Write a NumPy program that creates a 4D NumPy array and
# uses integer indexing to extract smaller subarrays.

import numpy as np
arr = np.array([[[[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]]]])

var = arr[0, 0, 0, :3]
print(var)