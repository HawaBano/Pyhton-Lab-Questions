# Create a numpy array and show how modifying a view modifies the original array.


import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

var = arr.view()
var[0, 0] = 99
print("Original array after modifying the view:")
print(arr)

print("\nView array:")
print(var)

