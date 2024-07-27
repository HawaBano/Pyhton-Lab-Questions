# Create a base class Animal with a method move. Implement subclasses Bird, Fish, and Mammal that override the move method with specific behaviors.

class Animal:

    def move(self):
        print("Moving...")


class Bird(Animal):

    def move(self):
        print("Flying in  the sky...")


class Fish(Animal):

    def move(self):
        print("Swimming in the water...")


class Mammal(Animal):

    def move(self):
        print("Walking on land...")


bird = Bird()
fish = Fish()
mammal = Mammal()

bird.move()
fish.move()
mammal.move()
