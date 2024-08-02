
# Create a 4x4 matrix with random values from an exponential distribution with scale 1.0.

import numpy as np

arr = np.random.exponential(1.0,size=(4,4))
print(arr)