# # Create a numpy array and demonstrate that reshaping a view affects the original array's shape.
#
#
import numpy as np

arr = np.arange(12).reshape(4, 3)
print("original array:\n",arr)
var = arr.view()
var = arr.reshape(3, 4)
var[0, 0] = 100
print("modified view:\n",var)
print("reshape array:\n",var)
print()
print("original array after modification:\n",arr)





# import numpy as np
#
#
# array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# # slicing array[start:stop]
# # print(array[1:4])
#
# # slicing array[start:stop:space]
# # print(array[0::4])
#
# # array = np.array([
# #     [
# #         [1, 2, 3, 4, 5],
# #         [6, 7, 8, 9, 10],
# #         [11, 12, 13, 14, 15]
# #     ],
# #     [
# #         [16, 17, 18, 19, 20],
# #         [21, 22, 23, 24, 25],
# #         [26, 27, 28, 29, 30]
# #     ],
# #     [
# #         [31, 32, 33, 19, 20],
# #         [21, 22, 23, 24, 25],
# #         [26, 27, 28, 29, 30]
# #     ]
# # ])
# #
# # # slicing array[start:stop:space] [2,3,4,7,8,9,17,18,19,22,23,24
# # print(array[::2,::2, ::2 ])
#
#
#
# array = np.array([1, 2, 3, 4, 5])
# #Binary Indexing
#
# print(array[[True, False, False, False, False]])
#
#
#
#
#
