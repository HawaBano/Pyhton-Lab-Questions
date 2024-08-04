# Use np.copy to create a copy of a structured array and demonstrate independent modification.

import numpy as np

dtype = [('name', 'U10'), ('age', 'i4'), ('score', 'f4')]
data = [('Ali', 25, 85.5), ('Bilal', 30, 90.0)]

arr = np.array(data, dtype=dtype)
print("original array:\n",arr)
var = np.copy(arr)
print("copy of arr:\n",var)

var[0]['age'] = 26
var[1]['score'] = 55

print("modified copy array",var)
print()
print("original array after modification\n",arr)