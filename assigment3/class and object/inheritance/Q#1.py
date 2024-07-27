# Implement a Shape class with a method to calculate the area. Create subclasses Circle, Rectangle, and Triangle that inherit from Shape and implement the area calculation specific to each shape.
import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
print("Area of circle:", circle.area())

rectangle = Rectangle(4, 5)
print("Area of rectangle:", rectangle.area())

triangle = Triangle(3, 6)
print("Area of triangle:", triangle.area())
