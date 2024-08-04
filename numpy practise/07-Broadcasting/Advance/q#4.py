# Broadcast a 1D array of shape (5,) to a 2D array of shape (3, 5) and perform
# element-wise division.


import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[10, 20, 30, 40, 50],
                     [15, 25, 35, 45, 55],
                     [20, 30, 40, 50, 60]])

result = arr1/ arr2
print("Result of element-wise division:")
print(result)
