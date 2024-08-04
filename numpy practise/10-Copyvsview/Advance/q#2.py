# Create a numpy array and demonstrate the difference between shallow and deep copies using np.copy.
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
shallow_copy = arr[:, :]
deep_copy = np.copy(arr)
shallow_copy[0, 0] = 99
deep_copy[1, 1] = 88

print("Original array:")
print(arr)
print("\nShallow copy:")
print(shallow_copy)
print("\nDeep copy:")
print(deep_copy)
