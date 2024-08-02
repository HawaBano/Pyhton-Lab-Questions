# Subtract the mean of each row of a numpy array.


import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
mean = np.mean(arr, axis=1)
result = arr - mean
print("Original Array:")
print(arr)

print("Row Means:")
print(mean)

print("Result After Subtracting Row Means:")
print(result)
