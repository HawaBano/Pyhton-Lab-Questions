# Generate an array of 5 random samples from the Poisson distribution with a lambda of 3.

import numpy as np
l = 3
arr = np.random.poisson(l ,size=5)
print(arr)