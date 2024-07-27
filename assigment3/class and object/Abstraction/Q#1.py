# Create an abstract class Shape with an abstract method calculate_area. Implement subclasses Circle, Rectangle, and Square that provide concrete implementations of calculate_area.
from abc import ABC, abstractmethod
import math

class Shape:

    @abstractmethod
    def calaulate_area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calculate_area(self):
        return self.length * self.length


circle = Circle(5)
print("Circle area: ", circle.calculate_area())

rectangle = Rectangle(4, 6)
print("Rectangle area:", rectangle.calculate_area())

square = Square(3)
print("Square area:", square.calculate_area())
