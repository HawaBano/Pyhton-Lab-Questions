# Concatenate three 2D numpy arrays along a new axis.

import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
array3 = np.array([[9, 10], [11, 12]])

c_array = np.concatenate((array1, array2, array3),axis=1)

print(c_array)

