# Design a Car class with attributes like model, year, and price. Implement methods to display car details and calculate the depreciation value over years.

class Car:
    model = ""
    year = 0
    price = 0

    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def display_details(self):
        print(f"""
              Model: {self.model}
              Year: {self.year}
              Price: {self.price}
              """)

    def deprieciation_value(self):
        depreciation_rate = 0.1
        current_year = 2024
        years_old = current_year - self.year
        depreciated_value = self.price * (1 - depreciation_rate) ** years_old
        print(depreciated_value)


car1 = Car("Toyota", 2012, 30000)
car1.display_details()
car1.deprieciation_value()
