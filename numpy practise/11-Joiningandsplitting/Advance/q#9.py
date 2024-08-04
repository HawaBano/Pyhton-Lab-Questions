# Split a 2D numpy array into multiple sub-arrays and recombine them using concatenate.

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

sub_array = np.split(array, 2)
print(sub_array)
print()
var = np.concat(sub_array)
print(var)
