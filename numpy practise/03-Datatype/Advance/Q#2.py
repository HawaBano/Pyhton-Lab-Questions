# Create a numpy array with dtype as datetime64 and check its data type.


import numpy as np

arr = np.array(['2024-01-01', '2024-01-02'],dtype='datetime64')
print(arr)
print(arr.dtype)