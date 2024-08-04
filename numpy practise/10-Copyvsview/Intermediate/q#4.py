# Create a numpy array and use the copy method to create an independent copy.
# Modify the copy and show the original is unchanged.



import numpy as np

arr = np.array([1,2,3,4,5])

var = arr.copy()
var[3] = 9
print(arr)
print(var)