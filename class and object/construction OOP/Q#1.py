class Bank_Account:
    def __init__(self, account_number, holder_name, starting_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance =starting_balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited: ", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print({f"""
 Account Number:{self.account_number}
 Account Holder:{self.holder_name}
 Current Balance:{self.balance}
"""})


s = Bank_Account(287456, "hawa", 1000)
s.deposit(500)
s.withdraw(200)
s.check_balance()
