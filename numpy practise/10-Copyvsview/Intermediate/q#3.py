# Create a numpy array and use slicing to create a view.
# Modify the slice and demonstrate that it affects the original array.


import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
slice_view = arr[1:, 1:]
print(slice_view)
print()
slice_view[0, 1] = 99
print(slice_view)
print()
print(arr)
