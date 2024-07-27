# Create a Customer class with private attributes for name, email, and phone number. Implement getter and setter methods to ensure encapsulation.

class Customer:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone


customer = Customer("sana", "sana123@gmail.com", "03123456")
print(f"""
    customer name : {customer.get_name()}
    customer email : {customer.get_email()}
    customer phone : {customer.get_phone()}
""")


customer.set_name("kinza")
customer.set_email("kinza@786")
customer.set_phone("039479163")

print(f"""
    customer name : {customer.get_name()}
    customer email : {customer.get_email()}
    customer phone : {customer.get_phone()}
""")
