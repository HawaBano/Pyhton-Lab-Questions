# Divide each element of a numpy array by the sum of all elements.

import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6]])
print(arr)
arr1= np.sum(arr)
print(arr1)
result = arr / arr1
print("\nResulting Array After Division:")
print(result)
