
class Appliance:

    def operate(self):
        pass


class WashingMachine(Appliance):

    def operate(self):
        return "Washing clothes..."


class Refrigerator(Appliance):

    def operate(self):
        return "Keeping food cool..."


class Microwave(Appliance):

    def operate(self):
        return "Heating food..."


def operate_appliances(appliances):
    for appliance in appliances:
        print(appliance.operate())
    print()


washing_machine = WashingMachine()
refrigerator = Refrigerator()
microwave = Microwave()

appliances = [washing_machine, refrigerator, microwave]
operate_appliances(appliances)
