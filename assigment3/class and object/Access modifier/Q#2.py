class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Balance after Deposited", self.__balance)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Balance after Withdrew", self.__balance)
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print("current amount", self.__balance)

    def display(self):
        print(f"""
            Account information
            account_number: {self.__account_number}
            holder_name: {self.__holder_name}
            balance: {self.__balance}
              """)


account = BankAccount("123456789", "ali", 500)
account.deposit(150)
account.withdraw(200)
account.check_balance()
account.display()
