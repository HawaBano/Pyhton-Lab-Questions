# Insert multiple values into a 1D numpy array at specified indices.

import numpy as np

arr = np.array([1,6, 7, 8 ])
var = np.insert(arr,1,[2, 3, 4, 5])
print(var)