# Generate a 4x4 matrix with random values from a normal distribution with mean 0 and standard deviation 1.

import numpy as np

arr = np.random.normal(0,1, size=(4,4))
print(arr)