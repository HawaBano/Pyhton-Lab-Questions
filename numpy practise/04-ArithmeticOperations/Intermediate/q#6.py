#
# Compute the dot product of two 1D numpy arrays.



import numpy as np

arr1 = np.array([1, 2, 3, 4, 7, 8])

arr1 = arr1.reshape(2,3)

print("Array1 is :",arr1)
arr2 = np.array([7, 8, 9, 10, 11, 23])
print("Array2 is :",arr2)

arr2 = arr2.reshape(3,2)

result = np.dot(arr1,arr2)
print("Dot product of array1 and array2\n",result)
