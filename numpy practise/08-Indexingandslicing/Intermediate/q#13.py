# Write a NumPy program that creates a 1D NumPy array and uses boolean indexing
# with logical operators (e.g., & for AND, | for OR)
# to select elements based on multiple conditions.

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
var1 = array[(array > 2) & (array < 6)]
print(array)
print(var1)


