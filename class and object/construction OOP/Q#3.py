# Implement a Course class that includes a constructor to initialize the course name, code, and an optional list of enrolled students.

class Course:
    e_stu = []

    def __init__(self, name, code, e_stu):
        self.name = name
        self.code = code
        self.e_stu = e_stu

    def display(self):
        print(f"""
        course name:{self.name}
        course code:{self.code}
        enrolled_student:{self.e_stu}
              """)


course = Course("python", "py132", ["hawa", "sana", "sara"])
course.display()
