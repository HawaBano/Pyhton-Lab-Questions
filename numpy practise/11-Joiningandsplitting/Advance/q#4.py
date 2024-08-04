# Split a 2D numpy array into multiple sub-arrays of different sizes along the first axis.

import numpy as np
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]])


sub_arrays = np.split(array, (2,5) )
