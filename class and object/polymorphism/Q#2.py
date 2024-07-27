# Implement a base class Shape with a method draw. Create subclasses Circle, Rectangle, and Triangle with specific implementations of the draw method. Demonstrate polymorphism by calling the draw method on a list of Shape objects.


class Shape():
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing Circle with radius {self.radius}")


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print("Drawing Rectangle with width  and height ", self.width, self.height)


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def draw(self):
        print("Drawing Triangle with base  and height ", self.base, self.height)


shape = Shape()
circle = Circle(5)
rectangle = Rectangle(4, 3)
triangle = Triangle(6, 4)
for i in (shape, circle, rectangle, triangle):
    i.draw()
