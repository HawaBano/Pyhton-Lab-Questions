# Create a numpy array with dtype='<U10' and store strings of length up to 10

import numpy as np

arr = np.array(["hello","world","python",'numpy'], dtype='<U10')

print(arr)