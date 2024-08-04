# Write a NumPy program that creates a 3D NumPy array and
# uses a combination of slicing and integer indexing to select
# a specific slice and then index into it.
import numpy as np

# Create the 3D NumPy array
array = np.array([[[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]]])


var = array[0:1,1:2,:]
print(var)

var2 = var[0:,0:,1:2]
print(var2)