# Create a hierarchical inheritance structure with a base class Employee and subclasses Manager and Developer. Implement methods specific to each subclass.


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_details(self):
        return (f"""
            Employee name: {self.name}
            Employee age: {self.age}
            Employee salary: {self.salary}
              """)


class Manager(Employee):
    team = ''

    def __init__(self, name, age, salary, team):
        super().__init__(name, age, salary)
        self.team = team

    def manage(self):
        return self.team

    def get_details(self):
        return (f"""
            manager name: {self.name}
            manager age: {self.age}
            manager salary: {self.salary}
            manager team: {self.team}
              """)


class Developer(Employee):
    language = ''

    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language

    def develop(self):
        return self.language

    def get_details(self):
        return (f"""
        developer name: {self.name}
        developer age: {self.age}
        developer salary:{self.salary}
        developer language: {self.language}
              """)


employee = Employee("sana", 30, 50000)
manager = Manager("sara", 43, 80000, "10 member of team")
manager.manage()
developer = Developer("ali", 40, 60000, "Python")
developer.develop()
print(employee.get_details())
print(manager.get_details())
print(developer.get_details())
