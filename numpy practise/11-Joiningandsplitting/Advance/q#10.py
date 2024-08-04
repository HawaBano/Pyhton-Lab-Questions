# Use split to divide a 3D numpy array into smaller 3D arrays along the first axis.

import numpy as np

array = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8]],
    [[9, 10, 11, 12], [13, 14, 15, 16]]])

var = np.split(array,2, axis=1)
print(var)
