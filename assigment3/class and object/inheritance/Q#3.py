# Design a Vehicle class with subclasses Car and Motorcycle. Implement methods specific to each subclass, such as num_wheels and engine_type.

class Vehical:
    num_wheels = ''
    num_engine = ''

    def __init__(self, num_wheels, engine_type):
        self.num_wheels = num_wheels
        self.engine_type = engine_type

    def get_num_wheels(self):
        return self.num_wheels

    def get_engine_type(self):
        return self.engine_type


class Car(Vehical):
    def __init__(self, engine_type):
        super().__init__(num_wheels=4, engine_type=engine_type)

    def set_num_wheels(self):
        return self.get_num_wheels()

    def set_engine_type(self):
        return self.get_engine_type


class Motorcycle(Vehical):
    def __init__(self, engine_type):
        super().__init__(num_wheels=2, engine_type=engine_type)

    def set_num_wheels(self):
        return self.get_num_wheels()

    def set_engine_type(self):
        return self.get_engine_type()


car = Car("Petrol")
print("car has ", car.num_wheels, "wheels and type of engine is", car.engine_type)


motor = Motorcycle("desile")
print("motorcycle has ", motor.num_wheels,
      "wheels and type of engine is", motor.engine_type)
