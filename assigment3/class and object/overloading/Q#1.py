# Implement a MathOperations class with overloaded methods for addition. The methods should handle addition of integers, floats, and lists of numbers.

from multipledispatch import dispatch


class MathOperator:
    @dispatch(int, int)
    def addition(a, b):
        print(f"Addition of two integer is :{a+b}")

    @dispatch(float, float)
    def addition(self, a, b):
        print(f"Addition of two float is :{a+b}")

    @dispatch(list)
    def addition(self, numbers):
        for number in (numbers):
            sum += number
            print(f"Addition of two float is :{sum}")


math = MathOperator()
math.addition(4, 8)
math.addition(6.2, 2.4)
math.addition([4, 6, 7, 9.3, 7.8])
