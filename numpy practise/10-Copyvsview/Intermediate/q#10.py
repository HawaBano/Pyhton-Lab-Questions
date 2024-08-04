# Use np.copy to create a copy of a structured array and demonstrate
# independent modification.


import numpy as np

dtype = [('id', 'i4'), ('name', 'U10'), ('age', 'i4')]
arr = np.array([(1, 'Ali', 30), (2, 'Bilal', 25), (3, 'Hamza', 35)], dtype=dtype)

var = np.copy(arr)
var[0]['name'] = 'Hassan'
var[1]['age'] = 28
print("Original array:")
print(arr)
print("\nCopy array with modifications:")
print(var)
