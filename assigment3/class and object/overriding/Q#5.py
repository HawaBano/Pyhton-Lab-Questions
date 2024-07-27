# Design a base class Appliance with a method power_usage. Implement subclasses WashingMachine and Oven that override the power_usage method with specific calculations.

class Appliance:
    brand = ''
    model = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_usage():
        pass


class WashingMachine(Appliance):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

    def power_usage(self):
        print(f"""
        brand name: {self.brand}
        model :{self.model}
        color: {self.color}
              """)


class Oven(Appliance):
    def __init__(self, brand, model, temperature):
        super().__init__(brand, model)
        self.temperature = temperature

    def power_usage(self):
        print(f"""
        brand name: {self.brand}
        model : {self.model}
        temperature : {self.temperature}
              """)


appliances = Appliance("haier", 2003)
washing_machine = WashingMachine("dawlance", 2024, "white")
oven = Oven("haier", 2023, "180C")

washing_machine.power_usage()
oven.power_usage()
