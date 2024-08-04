# Create a numpy array and use the base attribute to check if an array is a view or a copy.


import numpy as np

base_array = np.array([1, 2, 3, 4, 5])

view_array = base_array.view()
copy_array = base_array.copy()

print("Base array base:", base_array.base)
print("View array base:", view_array.base)
print("Copy array base:", copy_array.base)
