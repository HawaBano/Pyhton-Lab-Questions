# Create a numpy array and create a view of it.
# Modify the view and show that the original array is affected.

import numpy as np

arr = np.array([1,2,3,4,5])

var = arr.view()
var[3] = 9
print(arr)
print(var)