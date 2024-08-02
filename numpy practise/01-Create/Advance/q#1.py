# Create a numpy array with 100 logarithmically spaced points between 10^1 and 10^3.

import numpy as np

arr = np.logspace(1,3,num= 100, dtype='float')
print(arr)