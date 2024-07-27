class Product:
    name = ''
    price = ''
    stock_quantity = ''
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        self.stock_quantity += quantity


class Supplier:
    name = ''
    supplier_id = ''
    supplied_products = []
    def __init__(self, name, supplier_id):
        self.name = name
        self.supplier_id = supplier_id
        self.supplied_products = []

    def add_product(self, product):
        self.supplied_products.append(product)

class Inventory:
    product = {}
    products = {}
    def __init__(self):
        self.products = {}
        self.suppliers = {}

    def add_product(self, product):
        self.products[product.name] = product
        print("Product  added to inventory.", product.name)

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            print("Product  removed from inventory.", product_name)
        else:
            print("Product  not found in inventory.", product_name)

    def update_stock(self, product_name, quantity):
        if product_name in self.products:
            self.products[product_name].update_stock(quantity)
            print("Product stock updated to.", self.products[product_name].stock_quantity)
        else:
            print("Product  not found in inventory.")
    
    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print("Supplier  added to inventory.",supplier.name)

    def assign_product_to_supplier(self, supplier_id, product_name):
        if supplier_id in self.suppliers and product_name in self.products:
            supplier = self.suppliers[supplier_id]
            product = self.products[product_name]
            supplier.add_product(product)
            print("Product assigned for supplier with ", supplier.name)
        else:
            print("Supplier ID  or Product  not found in inventory.")

    def generate_inventory_report(self):
        print(" ------Inventory Report------")
        for product_name, product in self.products.items():
            print(f"Product: {product_name},Price: {product.price},Stock: {product.stock_quantity}")
        
        for supplier_id, supplier in self.suppliers.items():
            print(f"Supplier: {supplier.name},ID: {supplier_id},Supplied Products: {', '.join([p.name for p in supplier.supplied_products])}")



inventory = Inventory()
product1 = Product("Laptop", 1000, 50)
product2 = Product("Mobile", 500, 200)


supplier1 = Supplier("SupplyMan", "Suplier1")

inventory.add_product(product1)
inventory.add_product(product2)

inventory.add_supplier(supplier1)

inventory.assign_product_to_supplier("Suplier1", "Laptop")

inventory.update_stock("Laptop", 20)
inventory.update_stock("Mobile", -50)

inventory.generate_inventory_report()
