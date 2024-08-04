# Use dstack to concatenate two 3D numpy arrays along the depth axis.

import numpy as np

array1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
array2 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])
c_array = np.dstack((array1, array2))
print("Concatenated Array:")
print(c_array)



