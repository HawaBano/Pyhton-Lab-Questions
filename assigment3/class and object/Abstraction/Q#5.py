# Design an abstract class Appliance with an abstract method turn_on. Create subclasses WashingMachine, Refrigerator, and Oven that provide concrete implementations of turn_on.

from abc import ABC, abstractmethod


class Appliance:
    @abstractmethod
    def turn_on(self):
        pass


class Washing_Machine(Appliance):
    def turn_on(self):
        return "washing machine is turn on"


class Refrigerator(Appliance):
    def turn_on(self):
        return "Refrigerator is turn on"


class Oven(Appliance):
    def turn_on(self):
        return "Oven is turn on"


def turn_on(appliance=Appliance):
    print(appliance.turn_on())


machine = Washing_Machine()
print(machine.turn_on())

fridge = Refrigerator()
print(fridge.turn_on())

oven = Oven()
print(oven.turn_on())
