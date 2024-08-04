# Use the reshape method to swap the axes of a 3D numpy array.

import numpy as np
arr = np.arange(24).reshape((2, 3, 4))
print(arr)
print()
print()
var = arr.transpose(2, 1, 0)
print(var)