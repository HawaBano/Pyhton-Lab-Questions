# Design an interface Drivable with a method drive. Implement this interface in classes Car, Bike, and Truck with specific implementations of the drive method.

from abc import ABC, abstractmethod


class Driveable(ABC):
    @abstractmethod
    def drive(self):
        pass


class Car(Driveable):
    model = ''
    price = 0

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def drive(self):
        print(f"""

        car model : {self.model}
        car price : {self.price}
        """)


class Bike(Driveable):
    color = ''
    price = ''

    def __init__(self, color, price):
        self.color = color
        self.price = price

    def drive(self):
        print(f"""
        bike color : {self.color}
        bike price : {self.price}
              """)


class Truck(Driveable):
    price = ''
    model = ''
    engine = ''

    def __init__(self, price, model, engine):
        self.price = price
        self.model = model
        self.engine = engine

    def drive(self):
        print(f"""
        truck price :{self.price}
        truck model :{self.model}
        truck engine :{self.engine}
        """)


car = Car("2003", 300000)
bike = Bike("red", 40000)
truck = Truck(700000, "M2000", "petrol")

car.drive()
bike.drive()
truck.drive()
