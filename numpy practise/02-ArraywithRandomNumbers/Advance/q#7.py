#
# Generate a 1D array of 50 random numbers from a binomial distribution.

import numpy as np

arr = np.random.binomial(10,0.5,size=50)
print(arr)
