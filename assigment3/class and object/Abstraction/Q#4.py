# Create an abstract class Vehicle with an abstract method start_engine. Implement subclasses Car and Motorcycle with concrete implementations of start_engine.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        return "engine started"


class Motorcycle(Vehicle):
    def start_engine(self):
        return "engine started"


def start_engine(vehicle=Vehicle):
    print(vehicle.start_engine())


car = Car()
motor = Motorcycle()

start_engine(car)
start_engine(motor)
