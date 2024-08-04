# Write a NumPy program that creates a 2D NumPy array of random floats and uses boolean
# indexing to select elements that satisfy multiple conditions (e.g., greater than 0.5 and less than 0.8).


import numpy as np

arr = np.random.rand(2,2)

print((arr > 0.5) & (arr < 0.8))


