# Implement a BankAccount class with private attributes for account number, holder name, and balance. Ensure encapsulation by providing public methods for accessing and modifying these attributes.

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_holder_name(self):
        return self.__holder_name

    def set_holder_name(self, holder_name):
        self.__holder_name = holder_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance ")


account = BankAccount("123456789", "sara", 10000)
print(f"""
      Account number :{account.get_account_number()}
      Holder name :{account.get_holder_name()}
      current balance :{account.get_balance()}
""")
account.deposit(500)
print(f"""
      Account balamce after deposite :{account.get_balance()}

""")

account.withdraw(200)
print(f"""

      Account balance after withdraw :{account.get_balance()}
""")
