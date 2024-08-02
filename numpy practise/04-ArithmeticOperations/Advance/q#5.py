# Calculate the cumulative product of a numpy array.

import numpy as np

array = np.array([[1, 2, 3],[4, 5, 6]])

axis0 = np.cumprod(array, axis=0)

axis1 = np.cumprod(array, axis=1)

print("Cumulative product along axis 0:")
print(axis0)

print("\nCumulative product along axis 1:")
print(axis1)
