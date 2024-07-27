# Create a banking system with the following classes and features:
# A BankAccount class with attributes for account number, account holder, and balance. Implement methods for depositing, withdrawing, and checking the balance.
# A Customer class with attributes for name, customer ID, and a list of bank accounts.
# A Bank class to manage customers and their accounts. Implement methods to open accounts, close accounts, transfer funds between accounts, and get account details.



class BankAccount:
    account_number = ''
    account_holder = ''
    initial_balance = ''

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
    bank_accounts = {}
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.bank_accounts = {}
    
    def add_account(self, account):
        if account.account_number not in self.bank_accounts:
            self.bank_accounts[account.account_number] = account
            return True
        return False
    
    def remove_account(self, account_number):
        if account_number in self.bank_accounts:
            del self.bank_accounts[account_number]
            return True
        return False
    
    def get_account(self, account_number):
        return self.bank_accounts.get(account_number, None)
    
class Bank:
    customers = {}
    def __init__(self):
        self.customers = {}
    
    def add_customer(self, customer):
        if customer.customer_id not in self.customers:
            self.customers[customer.customer_id] = customer
            return True
        return False
    
    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
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
    
    def get_account_details(self, customer_id, account_number):
        customer = self.get_customer(customer_id)
        if customer:
            account = customer.get_account(account_number)
            if account:
                print(f"""
    Account Number: {account.account_number}
    Account Holder: {account.account_holder}
    Balance: {account.check_balance()}
                """)
        return None
    
bank = Bank()
customer1 = Customer("sana", 1)
customer2 = Customer("sara", 2)
bank.add_customer(customer1)
bank.add_customer(customer2)
bank.open_account(1, 101, "sana", 1000)
bank.open_account(2, 201, "sara", 500)

print(bank.get_account_details(1, 101))
print(bank.get_account_details(2, 201))

bank.close_account(1, 101)
   
