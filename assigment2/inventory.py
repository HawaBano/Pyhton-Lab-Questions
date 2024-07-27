class Product:
    name = ''
    price = ''
    stock_quantity = ''
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity


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
    products = {}
    suppliers = {}
    def __init__(self):
        self.products = {}
        self.suppliers = {}

    def add_product(self, product):
        if product.name in self.products:
            print("Product already exists. Use update_stock_quantity to modify stock.",product.name)
        else:
            self.products[product.name] = product
            print("Added product:",product)

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
            print("Removed product:",product_name)
        else:
            print("Product  not found in inventory.",product_name)

    def update_stock_quantity(self, product_name, quantity):
        if product_name in self.products:
            product = self.products[product_name]
            product.stock_quantity += quantity
            print(f"Updated stock for {product_name}: {product.stock_quantity}")
        else:
            print(f"Product {product_name} not found in inventory.")

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier
        print("Added supplier:",supplier)

    def generate_inventory_report(self):
        for product_name, product in self.products.items():
            print("""
                  "******Inventory Report******"
                Product: {product_name}
                Price: {product.price}
                Stock: {product.stock_quantity}
                  
                  """)
        
        for supplier_id, supplier in self.suppliers.items():
            print(f"""
                  ******Suppliers Report******
                Supplier: {supplier.name}
                ID: {supplier_id}
                Supplied Products: {', '.join([p.name for p in supplier.supplied_products])}
            """)



inventory = Inventory()

product1 = Product("Apple", 10, 5)
product2 = Product("Banana", 25, 10)


supplier1 = Supplier("Supply Man", "S001")

supplier1.add_product(product1)
supplier1.add_product(product2)
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_supplier(supplier1)

inventory.update_stock_quantity("Apple", 2)

inventory.remove_product("Banana")

inventory.generate_inventory_report()
