
class Animal:

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        return "Woof!"


class Cat(Animal):

    def speak(self):
        return "Meow!"


class Cow(Animal):

    def speak(self):
        return "Moo!"


def animal_speaks(animals):
    for animal in animals:
        print(animal.speak())
    


dog = Dog()
cat = Cat()
cow = Cow()


animals = [dog, cat, cow]
animal_speaks(animals)
