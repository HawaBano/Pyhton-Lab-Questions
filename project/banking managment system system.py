# Create a banking system with the following classes and features:
# A BankAccount class with attributes for account number, account holder, and balance. Implement methods for depositing, withdrawing, and checking the balance.
# A Customer class with attributes for name, customer ID, and a list of bank accounts.
# A Bank class to manage customers and their accounts. Implement methods to open accounts, close accounts, transfer funds between accounts, and get account details.


class BankAccount:
    account_number = ''
    account_holder = ''
    initial_balance = 0
    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def check_balance(self):
        return self.balance

class Customer:
    name = ''
    customer_id = ''
    bank_accounts = []
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.bank_accounts = []
    
    def add_account(self, account):
        if account.account_number not in [acc.account_number for acc in self.bank_accounts]:
            self.bank_accounts.append(account)
            return True
        return False
    
    def remove_account(self, account_number):
        for account in self.bank_accounts:
            if account.account_number == account_number:
                self.bank_accounts.remove(account)
                return True
        return False
    
    def get_account(self, account_number):
        for account in self.bank_accounts:
            if account.account_number == account_number:
                return account
        return None


class Bank:
    customers = []
    def __init__(self):
        self.customers = []
    
    def add_customer(self, customer):
        if customer.customer_id not in [cust.customer_id for cust in self.customers]:
            self.customers.append(customer)
            return True
        return False
    
    def remove_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                self.customers.remove(customer)
                return True
        return False
    
    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def open_account(self, customer_id, account_number, account_holder, initial_balance=0):
        customer = self.get_customer(customer_id)
        if customer:
            new_account = BankAccount(account_number, account_holder, initial_balance)
            customer.add_account(new_account)
            return True
        return False

    def close_account(self, customer_id, account_number):
        customer = self.get_customer(customer_id)
        if customer:
            customer.remove_account(account_number)
            return True
        return False
    
    def transfer_funds(self, from_customer_id, from_account_number, to_customer_id, to_account_number, amount):
        from_customer = self.get_customer(from_customer_id)
        to_customer = self.get_customer(to_customer_id)
        if from_customer and to_customer:
            from_account = from_customer.get_account(from_account_number)
            to_account = to_customer.get_account(to_account_number)
            if from_account and to_account:
                if from_account.withdraw(amount):
                    to_account.deposit(amount)
                    return True
                else:
                    print("Insufficient funds for transfer.")
            else:
                print("One or both accounts not found.")
        else:
            print("One or both customers not found.")
        return False

    def get_account_details(self, customer_id, account_number):
        customer = self.get_customer(customer_id)
        if customer:
            account = customer.get_account(account_number)
            if account:
                return f"""
    Account Number: {account.account_number}
    Account Holder: {account.account_holder}
    Balance: {account.check_balance()}
                """
        return "Account not found."

bank = Bank()
customer1 = Customer("Sana", 1)
customer2 = Customer("Sara", 2)
bank.add_customer(customer1)
bank.add_customer(customer2)
bank.open_account(1, 101, "Sana", 1000)
bank.open_account(2, 201, "Sara", 500)

print(bank.get_account_details(1, 101))
print(bank.get_account_details(2, 201))

print(bank.transfer_funds(1, 101, 2, 201, 200))

print(bank.get_account_details(1, 101))
print(bank.get_account_details(2, 201))

bank.close_account(1, 101)

bank.get_account_details(2, 201)

