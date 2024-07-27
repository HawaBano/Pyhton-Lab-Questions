# Implement an interface Payable with a method pay. Create classes Invoice, Salary, and Subscription that implement the pay method.

from abc import ABC, abstractmethod


class Payable:
    @abstractmethod
    def pay(self):
        pass


class Invoice(Payable):
    def __init__(self, invoice_number, amount):
        self.invoice_number = invoice_number
        self.amount = amount

    def pay(self):
        print("Paying invoice amount: ", self.amount)


class Salary(Payable):
    def __init__(self, employee_name, amount):
        self.employee_name = employee_name
        self.amount = amount

    def pay(self):
        print("Paying salary amount: ", self.amount)


class Subscription(Payable):
    def __init__(self, subscription_name, amount):
        self.subscription_name = subscription_name
        self.amount = amount

    def pay(self):
        print("Paying subscription amount:", self.amount)


invoice = Invoice("In123", 500)
salary = Salary("sana", 30000)
subscription = Subscription("subscription1", 20000)


invoice.pay()
salary.pay()
subscription.pay()
