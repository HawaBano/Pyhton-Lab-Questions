# Use np.insert to add elements to a 2D numpy array and specify the axis.

import numpy as np

# Original array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])


var = np.insert(arr, 1, [7, 8, 9], axis=0)

print(var)
