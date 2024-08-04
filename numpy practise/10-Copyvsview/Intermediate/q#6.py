# Create a 2D numpy array and create a view using np.view.
# Modify the view and show the changes in the original array.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:\n",arr)
var = arr.view()
var[0, 0] = 99
print("view after modification\n",var)
print("original array after modification\n",arr)
