# Create a Statistics class with overloaded methods for calculating the mean. The methods should handle lists of integers, floats, and nested lists.

from multipledispatch import dispatch
import statistics
class Statistics:
    @dispatch(list)
    def calculate(self, data):
        print("the calaulation of mean in integer:",statistics.mean(data))

    @dispatch(list)
    def calculate(self, data):
        print("the calaulation of mean in float:",statistics.mean(data))


    @dispatch(list)
    def calculate(self, data):
        print("the calaulation of mean  of nested list:",statistics.mean(data))

stats = Statistics()
stats.calculate([2,4,7,6])
stats.calculate([4.4, 5.7, 7.8])
stats.calculate([4.5,2,6, [4, 9.3,7.7]])



