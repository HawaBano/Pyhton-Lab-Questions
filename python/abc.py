class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
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
    
    def open_account(self, customer_id, account_number, initial_balance=0.0):
        customer = self.customers.get(customer_id, None)
        if customer:
            new_account = BankAccount(account_number, customer.name, initial_balance)
            return customer.add_account(new_account)
        return False
    
    def close_account(self, customer_id, account_number):
        customer = self.customers.get(customer_id, None)
        if customer:
            return customer.remove_account(account_number)
        return False
    
    def transfer_funds(self, from_customer_id, from_account_number, to_customer_id, to_account_number, amount):
        from_customer = self.customers.get(from_customer_id, None)
        to_customer = self.customers.get(to_customer_id, None)
        
        if from_customer and to_customer:
            from_account = from_customer.get_account(from_account_number)
            to_account = to_customer.get_account(to_account_number)
            
            if from_account and to_account:
                if from_account.withdraw(amount):
                    to_account.deposit(amount)
                    return True
        return False
    
    def get_account_details(self, customer_id, account_number):
        customer = self.customers.get(customer_id, None)
        if customer:
            account = customer.get_account(account_number)
            if account:
                return str(account)
        return "Account not found."

# Example usage
bank = Bank()

    # Adding customers
customer1 = Customer("Alice", "C001")
customer2 = Customer("Bob", "C002")
bank.add_customer(customer1)
bank.add_customer(customer2)

    # Opening accounts
bank.open_account("C001", "A001", 1000.0)
bank.open_account("C002", "A002", 500.0)

    # Checking account details
print(bank.get_account_details("C001", "A001"))  # Print details of Alice's account
print(bank.get_account_details("C002", "A002"))  # Print details of Bob's account

    # Depositing and withdrawing
customer1.get_account("A001").deposit(500.0)
customer2.get_account("A002").withdraw(200.0)

    # Transfer funds
bank.transfer_funds("C001", "A001", "C002", "A002", 300.0)

    # Checking updated account details
print(bank.get_account_details("C001", "A001"))  # Updated balance of Alice's account
print(bank.get_account_details("C002", "A002"))  # Updated balance of Bob's account

    # Closing account
bank.close_account("C002", "A002")
print(bank.get_account_details("C002", "A002"))  # Should indicate account not found
