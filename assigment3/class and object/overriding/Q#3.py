# Implement a base class Vehicle with a method fuel_efficiency. Create subclasses Car and Motorcycle that override the fuel_efficiency method with specific calculations.

class Vehicle:
    fuel_type = ''

    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def fuel_effifiency(self):
        pass


class Car(Vehicle):
    model = ''

    def __init__(self, fuel_type, model):
        super().__init__(fuel_type)
        self.model = model

    def fuel_effifiency(self):
        print(f"""
        car model: {self.model}
        fuel type: {self.fuel_type}
              """)


class Motorcycle(Vehicle):
    color = ''

    def __init__(self, fuel_type, color):
        super().__init__(fuel_type)
        self.color = color

    def fuel_effifiency(self):
        print(f"""
        fuel type : {self.fuel_type}
        motor cycle color : {self.color}
              """)


car = Car("m1023", "desel")
motorcycle = Motorcycle("petrol", "red")
car.fuel_effifiency()
motorcycle.fuel_effifiency()
