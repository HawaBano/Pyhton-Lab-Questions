
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"""
        name: {self.name}
        age: {self.age}
              """)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"""
        tetacher name: {self.name}
        teacher age: {self.age}
        teacher subject: {self.subject
                          }
              """)


class Student(Person):
    def __init__(self, name, age, grade_level):
        super().__init__(name, age)
        self.grade_level = grade_level

    def introduce(self):
        print(f"""
        student name: {self.name}
        student age : {self.age}
        student grade: {self.grade_level}
              """)
        
teacher = Teacher("sara", 35, "History")
student = Student("sana", 15, 10)
teacher.introduce()
student.introduce()
