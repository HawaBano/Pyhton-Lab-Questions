# Create a numpy array with mixed data types and check the resultant data type.

import numpy as np

arr = np.array([1.2,2,"hello",False])
print(arr)

print(arr.dtype)