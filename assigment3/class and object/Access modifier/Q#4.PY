# Implement a ShoppingCart class with private attributes for items (a list of item names). Provide public methods to add, remove, and list items in the cart.

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print("item removed")
        else:
            print(f"Item  not found in the cart.")

    def list_items(self):
        print(self.__items)


cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Orange")
cart.list_items()
cart.remove_item("Banana")
cart.list_items()
