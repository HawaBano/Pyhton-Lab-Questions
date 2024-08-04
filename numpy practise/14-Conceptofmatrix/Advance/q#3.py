# Solve a system of linear equations using a 3x3 matrix.
import numpy as np

A = np.array([
    [2, 3, 11],
    [4, 1, 2],
    [3, 5, 4]
])
b = np.array([1, 2, 3])
x = np.linalg.solve(A, b)
print(x)
