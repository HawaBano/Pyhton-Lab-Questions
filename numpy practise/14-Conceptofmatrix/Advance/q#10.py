# Compute the Kronecker product of two matrices.
import numpy as np

arr1 = np.array([[1, 2],
              [3, 4]])

arr2 = np.array([[0, 5],
              [6, 7]])

var = np.kron(arr1, arr2)

print(var)
