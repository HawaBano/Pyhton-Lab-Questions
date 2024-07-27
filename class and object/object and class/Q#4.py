# Create a Person class and a Student class that inherits from Person. Add attributes and methods specific to Student, such as student ID and GPA calculation.

class Person:
    name = ''
    age = 0
    gender = ''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"""
            Name:  {self.name}
            Age:", {self.age}
            Gender: {self.gender}

        """)


class Student(Person):

    def __init__(self, name, age, student_id, gender):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_gpa(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def info(self):
        print("Student ID:", self.student_id)
        print("GPA:", self.calculate_gpa())


student1 = Student("hawa", 20, "abc1234", "female")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(88)
student1.display_info()

student1.info()
