# Implement a DataProcessor class with overloaded methods for data sorting. The methods should handle sorting of lists of integers, floats, and strings.


from multipledispatch import dispatch


class DataProcess:
    @dispatch(list)
    def sort(self, data):
        print("sorted data of integer", sorted(data))

    @dispatch(list)
    def sort(self, num):
        print("sorted float data of list is:", sorted(num))

    @dispatch(list)
    def sort(self, num1):
        print("sorted string data of list is :", sorted(num1))


data = DataProcess()

data.sort([2, 9, 5, 7, 3])
data.sort([3.2, 8.5, 9.3])
data.sort(["cherry", "graps", "apple"])
