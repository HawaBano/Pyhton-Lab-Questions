# Add a scalar value to each element of a 4D numpy array of shape (2, 2, 2, 2).

import numpy as np


arr = np.array([[[[1, 2], [3, 4]],
                      [[5, 6], [7, 8]]],
                     [[[9, 10], [11, 12]],
                      [[13, 14], [15, 16]]]])

scalar = 10

result = arr+ scalar

print("Resulting array after adding scalar:")
print(result)
