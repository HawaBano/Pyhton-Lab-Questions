# Use broadcasting to perform element-wise addition of a 1D array [10, 20, 30] to each column of a 3x3 matrix.


import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

B = np.array([10, 20, 30])


result = A + B
print(result)
