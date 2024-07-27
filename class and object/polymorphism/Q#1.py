# Create a base class Employee with a method work. Implement subclasses Manager, Developer, and Designer with specific implementations of the work method. Demonstrate polymorphism by calling the work method on a list of Employee objects.

class Employee:
    def work(self):
        pass


class Manager(Employee):
    def work(self):
        print("the manager manage the team")


class Developer(Employee):
    def work(self):
        print("the developer written code")


class Designer(Employee):
    def work(self):
        print("the designer designe the user interface")


manager = Manager()
developer = Developer()
designer = Designer()
for i in (manager, developer, designer):
    i.work()
