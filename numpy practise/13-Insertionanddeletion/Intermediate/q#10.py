# Use np.delete to remove values from a 1D numpy array that are greater than a specified value.
import numpy as np

arr = np.array([1, 2, 3, 5, 6, 8])
var = np.delete(arr,(arr>3))
print(arr)
print()
print(var)