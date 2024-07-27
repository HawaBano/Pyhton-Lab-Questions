# Create a base class Shape with a method calculate_area. Implement subclasses Square and Triangle that override the calculate_area method with specific formulas.

import math


class Shape():
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):

        print(f"area of is", math.pi*self.radius**2)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print("area of Rectangle is:", self.width*self.height)


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        print("area of Triangle is:", 0.5 * self.base*self.height)


shape = Shape()
circle = Circle(5)
rectangle = Rectangle(4, 3)
triangle = Triangle(6, 4)
circle.calculate_area()
rectangle.calculate_area()
triangle.calculate_area()
