# Create a numpy array and demonstrate that views share the same data buffer.


import numpy as np

arr = np.arange(9).reshape(3, 3)
print("Original Array:\n",arr)
var = arr.view()
arr[0, 0] = 99
print("\nModified View Array:")
print(arr)
print("\nOriginal Array After Modifying View:")
print(arr)
print("buffer data",var.base is arr)



