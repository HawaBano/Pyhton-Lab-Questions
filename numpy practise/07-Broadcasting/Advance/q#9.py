# Broadcast a 3D array of shape (1, 3, 4) to a 2D array of shape (3, 4)
# and add them element-wise.

import numpy as np

arr1 = np.array([[[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]]])

arr2 = np.array([[10, 20, 30, 40],
                     [50, 60, 70, 80],
                     [90, 100, 110, 120]])


result = arr1 + arr2
print("Resulting array after element-wise addition:")
print(result)
