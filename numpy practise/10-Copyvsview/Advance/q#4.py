# Create a numpy array and use advanced indexing to create a view.
# Modify the view and show the impact on the original array.
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

var = arr.view()
var[0, 0] = 10
print(var)
print()
print(arr)
