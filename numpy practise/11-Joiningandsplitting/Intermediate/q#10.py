# Concatenate three 1D numpy arrays along the first axis.


import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr3 = np.array([9, 10, 11, 12])

var = np.concatenate((arr1,arr2,arr3),axis=0)
print(var)