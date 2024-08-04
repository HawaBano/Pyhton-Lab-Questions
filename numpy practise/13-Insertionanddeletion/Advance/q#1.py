# Insert a sub-array into a 2D numpy array at a specified index.

import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10]])

var = np.insert(arr,2,[11, 12, 13, 14, 15],axis=0)
print(arr)
print()
print(var)