# Use np.delete to remove rows from a 2D numpy array based on a condition.

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

var = np.sum(arr,axis= 0 ) >=10
var1 = np.delete(arr,var,axis=0)
print(var1)

