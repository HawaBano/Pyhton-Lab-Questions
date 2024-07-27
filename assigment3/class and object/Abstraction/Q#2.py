# Design an abstract class Employee with an abstract method calculate_salary. Implement subclasses FullTimeEmployee and PartTimeEmployee with concrete implementations of calculate_salary.

from abc import ABC, abstractmethod
import math


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        self.name = name
        self.annual_salary = annual_salary

    def calculate_salary(self):
        return self.annual_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


full_time_employee = FullTimeEmployee("sara", 60000)
print("Full-time employee salary:", full_time_employee.calculate_salary())

part_time_employee = PartTimeEmployee("ali", 20, 120)
print("Part-time employee salary:",  part_time_employee.calculate_salary())
