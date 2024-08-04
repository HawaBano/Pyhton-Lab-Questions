# Use hsplit to split a 2D numpy array into three parts along the second axis.


import numpy as np
arr = np.array([[1, 2, 3, 4, 5, 6]])
var = np.hsplit(arr,3)
print(var)
