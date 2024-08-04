# Create a numpy array and reshape it to a higher dimension (e.g., from 2D to 4D).
#

import numpy as np

arr = np.arange(12).reshape((2, 6))
print(arr)
arr2 = arr.reshape((1, 2, 3, 2))
print(arr2)
