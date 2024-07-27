# Create a Person class and subclasses Teacher and Student. Add attributes and methods specific to each subclass and demonstrate simple inheritance

class Person:
    name = ''
    age = None
    gender = ''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Teacher(Person):
    subject = ''

    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject
        print(f"""
        teacher name :{self.name}
        teacher age :{self.age}
        teacher gander :{self.gender}
        subject: {self.subject}

""")


class Student(Person):
    grade = ''

    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.grade = grade
        print(f"""
        teacher name :{self.name}
        teacher age :{self.age}
        teacher gander :{self.gender}
        grade: {self.grade}

""")


teacher = Teacher("zarah", 35, "female", "english")
print(teacher)

student = Student("sana", 20, "female", "B")
print(Student)
