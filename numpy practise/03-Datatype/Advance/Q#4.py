# Create a numpy array of unsigned integers and convert it to signed integers.


import numpy as np
arr = np.array([1,2,3,4],dtype=np.uint8)

print(arr)
print(arr.dtype)

var = arr.astype(np.int8)
print(var)
print(var.dtype)