# Delete multiple values from a 1D numpy array at specified indices.

import numpy as np

arr = np.array([1, 2, 3, 5, 6, 8])
var = np.delete(arr,(2,3,4))
print(arr)
print()
print(var)