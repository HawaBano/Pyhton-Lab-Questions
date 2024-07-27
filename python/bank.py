class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited amount to account :", self.balance)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew amount from account:", self.balance)
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account balance:", self.balance)
        return self.balance


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account  added for customer:",self.name)

    def remove_account(self, account_number):
        account_to_remove = None
        for account in self.accounts:
            if account.account_number == account_number:
                account_to_remove = account
                break
        if account_to_remove:
            self.accounts.remove(account_to_remove)
            print("Account removed from customer", self.name)
        else:
            print("Account not found for customer", self.name)

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None


class Bank:
    customers = []
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer  added", customer.name)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def remove_customer(self, customer_id):
        customer_to_remove = None
        for customer in self.customers:
            if customer.customer_id == customer_id:
                customer_to_remove = customer
                break
        if customer_to_remove:
            self.customers.remove(customer_to_remove)
            print("Customer removed.", customer_to_remove.name)
        else:
            print("Customer with ID not found.")

    def open_account(self, customer_id, account_number, initial_balance):
        customer = self.get_customer(customer_id)
        if customer:
            new_account = BankAccount(account_number, customer.name, initial_balance)
            customer.add_account(new_account)
            print("Account  opened for customer with initial balance ",initial_balance)
        else:
            print(f"Customer with ID  not found.")

    def close_account(self, customer_id, account_number):
        customer = self.get_customer(customer_id)
        if customer:
            customer.remove_account(account_number)
        else:
            print(f"Customer with ID  not found.")

    def transfer_funds(self, from_account_number, to_account_number, amount):
        from_account, to_account = None, None
        for customer in self.customers:
            from_account = customer.get_account(from_account_number)
            if from_account:
                break
        for customer in self.customers:
            to_account = customer.get_account(to_account_number)
            if to_account:
                break
        if from_account and to_account and from_account.balance >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f"Transferred amount  from account  to account successfully")
        else:
            print("Transfer failed. Check accounts and balance.")

    def get_account_details(self, account_number):
        for customer in self.customers:
            account = customer.get_account(account_number)
            if account:
                print(f"""
            Account Number: {account.account_number}
            Account Holder: {account.account_holder}
            Balance: {account.balance}
            """)
                return account
        print(f"Account  not found.")
        return None

bank = Bank()
customer1 = Customer("Ali", "C001")
customer2 = Customer("Hamza", "C002")

bank.add_customer(customer1)
bank.add_customer(customer2)

bank.open_account("C001", "A1001", 500)
bank.open_account("C002", "A2001", 750)

bank.get_account_details("A1001")
bank.get_account_details("A2001")

customer1.get_account("A1001").deposit(200)
customer1.get_account("A1001").withdraw(100)

bank.transfer_funds("A1001", "A2001", 300)

bank.close_account("C001", "A1002")
bank.remove_customer("C002")
