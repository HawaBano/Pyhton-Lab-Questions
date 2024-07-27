# Implement a multi-level inheritance hierarchy with classes Animal, Mammal, and Dog. Add attributes and methods specific to each class and demonstrate multi-level inheritance.


class Animal:
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def make_sound(self):
        print("my dog make a sound", self.sound)


class Dog(Mammal):
    def __init__(self, name, type_dog):
        super().__init__(name, "Woof")
        self.type_dog = type_dog

    def dog_color(self):
        print("my dog color is black and white")


my_dog = Dog("honey", "Buldog")
print(f"My dog's name is", my_dog.name)
print(f"It is a type of.", my_dog.type_dog)
my_dog.make_sound()
my_dog.dog_color()
