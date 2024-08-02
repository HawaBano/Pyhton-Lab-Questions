# Compute the cross product of two 3-dimensional vectors.

import numpy as np


arr1= np.array([[[1, 2, 3]]])
print(arr1.ndim)
arr2 = np.array([[[4, 5, 6]]])
arr3 = np.cross(arr1,arr2)

print("The cross product is:", arr3)
