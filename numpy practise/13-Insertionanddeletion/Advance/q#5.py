# Use np.append to add rows to a 2D numpy array.


import numpy as np

arr = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

var = np.append(arr,[[13, 14, 15, 16]],axis=0)
print(arr)
print()
print(var)