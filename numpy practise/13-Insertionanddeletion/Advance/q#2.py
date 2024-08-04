# Use np.insert to add elements to a 1D numpy array at specified positions and specify the axis.

import numpy as np

arr = np.array([1, 2, 3, 8, 9])
var = np.insert(arr,3,[4, 5, 6, 7],axis=0)
print(var)