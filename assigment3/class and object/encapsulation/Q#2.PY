# Create a Student class with private attributes for name, student ID, and GPA. Implement getter and setter methods to access and modify these attributes

class Student:
    __name = ''
    __student_id = ''
    __gpa = ''

    def __init__(self, __name, __student_id, __gpa):
        self.__name = __name
        self.__student_id = __student_id
        self.__gpa = __gpa

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            print("GPA must be between 0.0 and 4.0")


student = Student("sara", "CS123", 3.5)

print(f"""
    student1 name : {student.get_name()}
    student1 ID : {student.get_student_id()}
    student1 gpa : {student.get_gpa()}
      """)


student.set_name("hawa")
student.set_student_id("CS345")
student.set_gpa(3.3)

print(f"""
    student1 name : {student.get_name()}
    student1 ID : {student.get_student_id()}
    student1 gpa : {student.get_gpa()}
      """)
