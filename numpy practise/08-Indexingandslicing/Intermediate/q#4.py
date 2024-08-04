# Write a NumPy program that creates a 4D NumPy array and uses multi-dimensional
# indexing to select a subarray.


import numpy as np

arr = np.array([[[
            [ 0,  1],
            [ 2,  3]]]])
var = arr[:,:,1:,:]

print(var)
