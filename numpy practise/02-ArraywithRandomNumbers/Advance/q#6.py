# Generate a 5x5 array of random numbers and replace all numbers greater than 0.5 with 1 and the
#     rest with 0.


import numpy as np

arr = np.random.rand(5,5)
print(arr)

arr2 = np.where(arr>0.5,1,0)
print(arr2)