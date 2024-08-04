# Concatenate two 1D numpy arrays along the first axis.

import numpy as np

arr = np.array([1, 2, 3, 4])
arr1 = np.array([5, 6, 7, 8])
var = np.concatenate((arr,arr1))
print(var)
