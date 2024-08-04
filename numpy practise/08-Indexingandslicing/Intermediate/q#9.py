#Write a NumPy program that creates two 1D NumPy arrays and uses np.ix_ to
# perform cross-indexing on a 2D array.

import numpy as np
arr3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

var = np.ix_([0,2],[0,1])
result = arr3[var]
print(result)
