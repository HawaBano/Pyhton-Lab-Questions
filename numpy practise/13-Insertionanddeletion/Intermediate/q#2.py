# Insert a row into a 2D numpy array at a specified index.

import numpy as np
arr = np.array([[1, 2, 3],[ 5, 6, 7]])
var = np.insert(arr,2,[[8, 9, 10]],axis=0)
print(var)