# Convert a numpy array of datetime64 to a numpy array of timedelta64.


import numpy as np

arr = np.array(['2024-01-01', '2024-01-02'],dtype='datetime64')
print(arr)
print(arr.dtype)

var = arr.astype(dtype='timedelta64')
print(var.dtype)