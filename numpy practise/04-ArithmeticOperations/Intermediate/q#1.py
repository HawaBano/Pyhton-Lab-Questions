# Create two numpy arrays of shape (3, 3) and perform element-wise addition.

import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Array1 is :",arr1)
arr2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Array2 is :",arr2)

result = arr1 + arr2

print("Addition of array1 and array2\n",result)