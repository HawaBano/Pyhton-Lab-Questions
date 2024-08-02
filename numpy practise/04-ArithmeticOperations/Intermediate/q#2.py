#
# Subtract two numpy arrays of shape (2, 2).

import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print("Array1 is :",arr1)
arr2 = np.array([[9, 8, 7], [6, 5, 4]])
print("Array2 is :",arr2)

result = arr1 - arr2

print("Subtraction  of array1 and array2\n",result)