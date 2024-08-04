# Concatenate two 2D numpy arrays along the second axis.

import numpy as np

arr1 = np.array([
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12]
                ])
arr2 = np.array([
                [13, 14, 15, 16],
                [17, 18, 19, 20]
                ])
var = np.concatenate((arr1,arr2), axis=1)
print(var)