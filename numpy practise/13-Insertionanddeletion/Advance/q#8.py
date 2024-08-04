# Delete elements from a 3D numpy array at specified positions.
#
import numpy as np

arr = np.array([[
                 [1, 2, 3, 4],
                 [5, 6, 7, 8]],

                [ [9, 10, 11, 12],
                 [11, 12, 13, 14]]
                ])

var = np.delete(arr,0,axis=0)
print(var)

