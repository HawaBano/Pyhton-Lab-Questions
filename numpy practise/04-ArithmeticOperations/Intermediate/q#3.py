
# Multiply two numpy arrays of shape (3, 2).

import numpy as np

arr1 = np.array([[1, 2], [3, 4], [5, 6]])

arr1 = arr1.reshape(2,3)

print("Array1 is :",arr1.shape)
arr2 = np.array([[7, 8], [9, 10], [11, 12]])
print("Array2 is :",arr2)

result = arr1 * arr2

print("Multipication of array1 and array2\n",result)