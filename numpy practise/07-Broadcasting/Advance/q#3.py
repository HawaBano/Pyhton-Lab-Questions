# Use broadcasting to add a 1D array to each slice of a 3D numpy array of shape (3, 4, 5).


import numpy as np

arr = np.array([[[ 1,  2,  3,  4,  5],
                      [ 6,  7,  8,  9, 10],
                      [11, 12, 13, 14, 15],
                      [16, 17, 18, 19, 20]],

                     [[21, 22, 23, 24, 25],
                      [26, 27, 28, 29, 30],
                      [31, 32, 33, 34, 35],
                      [36, 37, 38, 39, 40]],

                     [[41, 42, 43, 44, 45],
                      [46, 47, 48, 49, 50],
                      [51, 52, 53, 54, 55],
                      [56, 57, 58, 59, 60]]])


arr1 = np.array([1, 2, 3, 4, 5])

result = arr + arr1
print("1D array:")
print(arr1)
print("Result of addition:")
print(result)
