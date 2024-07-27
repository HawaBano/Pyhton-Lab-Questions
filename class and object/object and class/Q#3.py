# Implement a Vector class to represent a mathematical vector with methods for addition, subtraction, dot product, and magnitude calculation.

class Vector:
    x = 0,
    y = 0,
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def addition(self, vactor):
        return (self.x+vactor.x,  self.y+vactor.y, self.z+vactor.z)

    def subtraction(self, vactor):
        return (self.x-vactor.x,  self.y-vactor.y, self.z-vactor.z)

    def dot_product(self, vactor):
        return (self.x*vactor.x,  self.y*vactor.y, self.z*vactor.z)

    def magnitude(self, vactor):
        return (self.x**vactor.x,  self.y**vactor.y, self.z**vactor.z)


vactor_a = Vector(9, 8, 7)
vactor_b = Vector(4, 5, 3)

vactor_c = vactor_a.addition(vactor_b)
print("the addition of vactor is :", vactor_c)

vactor_c = vactor_a.subtraction(vactor_b)
print("the subtraction of vactor is :", vactor_c)

vactor_c = vactor_a.dot_product(vactor_b)
print("the dot product of vactor is :", vactor_c)

vactor_c = vactor_a.magnitude(vactor_b)
print("the magnitude of vactor is :", vactor_c)
