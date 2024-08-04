# Create a 3D numpy array and create a view of a sub-array.
# Modify the view and show the impact on the original array.

import numpy as np

arr = np.array([[[1, 2, 3],
                            [4, 5, 6]],
                           [[13, 14, 15],
                            [16, 17, 18]]])

print("Original Array:")
print(arr)
view_array = arr.view()

view_array[0, 0, 0] = 999
print("\nModified View Array:")
print(view_array)
print("\nOriginal Array After Modification:")
print(arr)

