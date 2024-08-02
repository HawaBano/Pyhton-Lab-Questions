# Perform element-wise multiplication of two numpy arrays and then sum the result.


import numpy as np

arr = np.array([1, 2, 3,4])
print(arr)
arr1 = np.array([5, 6,7, 8])
print(arr1)

mul = np.multiply(arr,arr1)
print("multiplication of array:",mul)

total = np.sum(mul)
print(total)

