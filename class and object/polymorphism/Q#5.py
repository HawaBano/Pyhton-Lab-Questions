
class Vehicle:

    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        return "Starting car engine..."


class Bike(Vehicle):

    def start(self):
        return "Starting bike engine..."


class Boat(Vehicle):

    def start(self):
        return "Starting boat engine..."


def start_vehicles(vehicles):
    for vehicle in vehicles:
        print(vehicle.start())
    print()


car = Car()
bike = Bike()
boat = Boat()

vehicles = [car, bike, boat]
start_vehicles(vehicles)
