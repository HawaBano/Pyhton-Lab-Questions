# Add a 2D array of shape (4, 1) to a 3D array of shape (4, 3, 1) using broadcasting.


import numpy as np


A = np.array([[1], [2], [3], [4]])

B = np.array([[[5], [6], [7]],
              [[8], [9], [10]],
              [[11], [12], [13]],
              [[14], [15], [16]]])

result = B + A

print("Result of B + A:")
print(result)
