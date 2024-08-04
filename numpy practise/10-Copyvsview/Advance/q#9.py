# Create a numpy array and use slicing to create a sub-array view.
# Show that changes to the sub-array are reflected in the original array.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("original array\n",arr)

c_arr = arr.copy()
print("copy of original array:\n",c_arr)

var = c_arr.reshape((3, 2))
print("Reshaped copied array:\n",var)
print("Original array after reshaping the copy:\n")
print(arr)
