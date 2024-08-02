# Create a structured numpy array with fields 'name' (string), 'age' (int), and 'weight' (float).


import numpy as np

dt = np.dtype([('name',str),('age',int),('wieght',float)])
arr = np.array([('Sana', 2, 21.0),('Sara', 3, 11.0)])
print(arr)
print(arr.dtype)