# Use broadcasting to subtract the column mean of a 2D array from each element in
# the array.

import numpy as np

arr = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

c_mean = np.mean(arr, axis=1)

result = arr - c_mean

print("Column means:")
print(c_mean)
print("Resulting array after subtracting column mean:")
print(result)
