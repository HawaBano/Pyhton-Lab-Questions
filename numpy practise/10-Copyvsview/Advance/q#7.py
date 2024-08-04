# Use np.copy to create a copy of a large numpy array and demonstrate memory independence.
import numpy as np

arr = np.arange(9).reshape(3, 3)
print("Original Array:\n",arr)
var = arr.copy()
arr[0, 0] = 99
print(arr)
print("\nOriginal Array After Modifying View:")
print(arr)
