# Design a Calculator class with overloaded methods for multiplication. The methods should handle multiplication of integers, floats, and lists of numbers.

from multipledispatch import dispatch


class Multipliction:
    @dispatch(int, int)
    def multiply(self, a, b):
        print(f"multiplication of two integer is :{a*b}")

    @dispatch(float, float)
    def multiply(self, a, b):
        print(f"multiplication of two float is :{a*b}")

    @dispatch(list)
    def multiply(self, numbers):
        for number in (numbers):
            mul = 1
            mul *= number
        print(f"multiplication of a list is :{mul}")

mul = Multipliction()
mul.multiply(5,6)
mul.multiply(5.3, 6.2)
mul.multiply([2, 4,5.3, 6])
