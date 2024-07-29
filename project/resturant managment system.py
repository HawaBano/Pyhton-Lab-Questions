class MenuItem:
    def __init__(self, name, price, availability=True):
        self.name = name
        self.price = price
        self.availability = availability

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.ordered_items = []

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.ordered_items = []

    def add_item(self, item):
        self.ordered_items.append(item)


class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.customers = {}
        self.orders = {}

    def add_menu_item(self, name, price, availability=True):
        if name not in self.menu_items:
            self.menu_items[name] = MenuItem(name, price, availability)
            print(f"Menu item  added.")
        else:
            print(f"Menu item  already exists.")

    def register_customer(self, name, customer_id):
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(name, customer_id)
            print(f"Customer  registered with ID")
        else:
            print(f"Customer ID  already exists.")

    def place_order(self, customer_id):
        if customer_id in self.customers:
           customer = self.customers[customer_id]
           order_id = len(self.orders) + 1
           order = Order(order_id, customer)  
           return "Order  placed successfully!",order_id
        else:
            return "customer id not found"
    
    

    def handel_process_order(self, order_id):
        if order_id not in self.orders:
            print(f"Order ID  not found.")
        else:       
          return  "Processing order  for customer" ,order_id



restaurant = Restaurant()
restaurant.add_menu_item("Burger", 50)
restaurant.add_menu_item("Fries", 20)


restaurant.register_customer("Ali", 1)
restaurant.register_customer("Bilal", 2)

order1_id = restaurant.place_order(1)

print(restaurant.handel_process_order(order1_id))