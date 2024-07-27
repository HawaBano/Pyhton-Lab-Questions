# Create a BankAccount class with attributes for account number, holder name, and balance. Implement methods for depositing, withdrawing, and checking balance. Ensure that withdrawing does not allow the balance to go negative

class Bank_Account:
    account_number = 0
    holder_name = ""
    balance = 0

    def __init__(self, account_number, holder_name):
        self.balance = 0
        self.account_number = account_number
        self.holder_name = holder_name

    def deposit(self):

        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print("Amount deposited is :", amount)
        else:
            print("you enter invalid balance")

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance ")

    def check_balance(self):
        print("Net Available Balance=", self.balance)


s = Bank_Account(287456, "hawa")
s.deposit()
s.withdraw()
s.check_balance()
