# Reshape a 3x4 numpy array to a 2x6 array.

import numpy as np

arr = np.array([[1, 2 ,3 ,4] ,
                [5 ,6 ,7 ,8 ],
                [9, 10, 1, 2]])
var = arr.reshape(2,6)
print(var)