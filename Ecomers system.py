# Design and implement an e-commerce system with the following classes and features:
# A Product class with attributes for name, price, and stock quantity.
# A Customer class with attributes for name, email, and a shopping cart (a list of products).
# An Order class with attributes for order ID, customer, and a list of purchased products.
# An EcommercePlatform class to manage products, customers, and orders. Implement methods to add products, register customers, place orders, and check product availability.


class Product:
    name = ''
    price = 0
    stock_quantity = 0
    
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
    
    def update_stock(self, quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            return True
        return False

class Customer:
    name = ''
    email = ''
    shopping_cart = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = []

    def add_to_cart(self, product):
        self.shopping_cart.append(product)
    
    def empty_cart(self):
        self.shopping_cart = []


class Order:
    order_counter = 1

    def __init__(self, customer, products):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.customer = customer
        self.products = products

    def display_order(self):
        print(f"""
              Order ID: {self.order_id}
              Customer: {self.customer.name} 
              customer email:{self.customer.email}""")
        for product in self.products:
            print(f"""
            product:{product.name}
            Price: {product.price}
 """)

class EcommercePlatform:
    def __init__(self):
        self.products = []
        self.customers = []
        self.orders = []

    def add_product(self, name, price, stock_quantity):
        product = Product(name, price, stock_quantity)
        self.products.append(product)
    
    def register_customer(self, name, email):
        customer = Customer(name, email)
        self.customers.append(customer)

    def check_product_availability(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product.stock_quantity > 0
        return False
    
    def place_order(self):
        customer = None
        purchased_products = []
        for product in customer.shopping_cart:
            if product.update_stock(1):
                purchased_products.append(product)
            else:
                print(f"Product  is out of stock")
        
        if purchased_products:
            order = Order(customer, purchased_products)
            self.orders.append(order)
            customer.empty_cart()
            print(f"Order  placed ")
        else:
            print("No products were purchased")

    def display_products(self):
        for product in self.products:
            print(f"""
        Available products:
        product: {product.name} 
        Price: {product.price}
        Stock: {product.stock_quantity}
""")

    def display_customers(self):
        for customer in self.customers:
            print(f"""
            Registered customers:
        customer name: {customer.name} 
        customer email: {customer.email}
""")


ecomers = EcommercePlatform()

ecomers.add_product("Laptop", 1500, 10)
ecomers.add_product("Phone", 800, 5)


ecomers.register_customer("ali", "ali123@gmail.com")
ecomers.register_customer("sana", "sana123@gmail.com")

for customer in ecomers.customers:
    if customer.name == "sana":
        customer.add_to_cart(ecomers.products[0])
        customer.add_to_cart(ecomers.products[1])

ecomers.display_products()
ecomers.display_customers()

ecomers.place_order()

for order in ecomers.orders:
    order.display_order()
print(ecomers.check_product_availability("Laptop")," Laptop available")

