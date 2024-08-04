# Concatenate a list of 1D numpy arrays into a single 2D array along the first axis.


import numpy as np

array = [np.array([1, 2, 3]),
              np.array([4, 5, 6]),
              np.array([7, 8, 9])]

var = np.vstack(array)
print(var)
