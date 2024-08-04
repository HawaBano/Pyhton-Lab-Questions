# Use np.linalg.svd to perform singular value decomposition on a 3x3 matrix.
# Compute SVD

import numpy as np

arr = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

var = np.linalg.svd(arr)

print(var)