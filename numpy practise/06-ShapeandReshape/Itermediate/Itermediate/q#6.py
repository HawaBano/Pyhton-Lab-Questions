# Create a 2D numpy array and change its shape to (1, 6).

import numpy as np

arr = np.array([[2, 4, 5],
                [ 6, 7, 8]])
var = arr.reshape(1,6)
print(var)