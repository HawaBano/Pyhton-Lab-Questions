# Stack a list of 2D numpy arrays along a new axis.
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.array([[9, 10], [11, 12]])
var = [arr1, arr2, arr3]
stack = np.stack(var, axis=1)

print("Stacked Array:")
print(stack)
