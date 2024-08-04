#
# Reshape a numpy array of shape (12 ,) into multiple compatible shapes
# using reshape with -1 for automatic dimension calculation.

import numpy as np

arr = np.arange(12)
reshaped = arr.reshape(-1, 3)
print(reshaped)
