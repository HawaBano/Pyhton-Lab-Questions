# Reshape a numpy array and use the order parameter to
# specify row-major (C-style) or column-major (Fortran-style) order

import numpy as np

arr = np.arange(12)
c = arr.reshape((3, 4), order='C')
print(c)

f = arr.reshape((3, 4), order='F')
print(f)
