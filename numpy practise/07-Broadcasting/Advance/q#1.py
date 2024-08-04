# Use broadcasting to normalize a 2D numpy array by subtracting the mean of each row.
#
import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6]])

means = np.mean(arr)

var = arr - means

print("Original array:")
print(arr)
print("Row means:")
print(means)
print("Normalized array:")
print(var)
