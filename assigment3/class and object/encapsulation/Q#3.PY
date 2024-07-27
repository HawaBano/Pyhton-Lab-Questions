# Design a Product class with private attributes for name, price, and stock quantity. Provide public methods to get and set these attributes, ensuring encapsulation.

class Product:

    __name = ''
    __price = 0
    __stock_quantity = 0

    def __init__(self, __name, __price, __stock_quantity):
        self.__name = __name
        self.__price = __price
        self.__stock_quantity = __stock_quantity

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("the price is negative")

    def get_quantity(self):
        return self.__stock_quantity

    def set_quantity(self, quantity):
        if quantity > 0:
            self.__stock_quantity = quantity
        else:
            print("enter the positive number")


product = Product("laptop", 60000, "2")

print(f"""

    product name : {product.get_name()}
    product price : {product.get_price()}
    product quantity : {product.get_quantity()}
      """)

product.set_name("moblie")
product.set_price(3000)
product.set_quantity(4)


print(f"""

    product name : {product.get_name()}
    product price : {product.get_price()}
    product quantity : {product.get_quantity()}
      """)
