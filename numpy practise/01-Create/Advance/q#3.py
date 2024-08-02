# Create a 5x5 matrix with 1 on the border and 0 inside.

import numpy as np

var = np.zeros((5, 5), dtype=int)

var[0, :] = 1
var[-1, :] = 1
var[:, 0] = 1
var[:, -1] = 1

print(var)

