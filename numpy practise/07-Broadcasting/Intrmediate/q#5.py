# Add a 1D array of shape (4,) to each row of a 2D array of shape (4, 4).

import numpy as np


arr1 = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])


arr2 = np.array([10, 20, 30, 40])


result = arr1 + arr2

print(result)
