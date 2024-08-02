# Compute the element-wise natural logarithm of one plus each element (log1p) in a numpy array.


import numpy as np

arr = np.array([2,3,5,7,4])
var = np.log1p(arr)
print(var)