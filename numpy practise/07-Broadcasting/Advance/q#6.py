# Perform element-wise multiplication of a 4D numpy array of shape (2, 3, 1, 4)
# with a 2D array of shape (3, 4).


import numpy as np


A = np.array([[[[1, 2, 3, 4]],
               [[5, 6, 7, 8]],
               [[9, 10, 11, 12]]],

              [[[13, 14, 15, 16]],
               [[17, 18, 19, 20]],
               [[21, 22, 23, 24]]]])

B = np.array([[5, 1, 2, 3.],
              [4, 12, 6, 7],
              [8, 9, 10, 11]])


result = A * B
print("Result of A * B:")
print(result)
