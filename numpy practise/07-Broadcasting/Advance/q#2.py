# Perform element-wise multiplication of a 3D array of shape (2, 3, 4)
# with a 1D array of shape (4,).


import numpy as np

arr = np.array([[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]],
                     [[13, 14, 15, 16],[17, 18, 19, 20],[21, 22, 23, 24]]])

arr1 = np.array([1, 2, 3, 4])
result = arr * arr1

print("3D array:")
print(arr)
print("1D array:")
print(arr1)
print("Result of element-wise multiplication:")
print(result)
