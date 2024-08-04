# Create a 1D numpy array of 10 elements and reshape it to a 2x5 array.
#

import numpy as np

arr = np.array([1, 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10])
var = arr.reshape(2,5)
print(var)