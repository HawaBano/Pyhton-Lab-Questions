# Create a numpy array and set the element in the center to 1 and all other elements to 0.
# 

import  numpy as np

array = np.zeros((5,5))
# array[0:3,4:3] = 1

array[:3] = 1

# Set the last 3 elements to 1
array[-3:] = 1

print(array)
