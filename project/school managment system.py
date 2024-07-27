# # Create a school management system with the following classes and features:
# # A Person base class with attributes for name, age, and address.
# # A Student class that inherits from Person and adds attributes for student ID, grade, and a list of enrolled courses.
# # A Teacher class that inherits from Person and adds attributes for employee ID, subject, and a list of assigned courses.
# # A Course class with attributes for course name, course code, and a list of enrolled students.
# # A School class to manage students, teachers, and courses. Implement methods to add students, add teachers, assign courses, and enroll students in courses.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Student(Person):
    def __init__(self, name, age, address, student_id, grade):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grade = grade
        self.enrolled_courses = []

class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject
        self.assigned_courses = []

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = []

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def assign_course(self, teacher, course):
        teacher.assigned_courses.append(course)

    def enroll_student_in_course(self, student, course):
        student.enrolled_courses.append(course)
        course.enrolled_students.append(student)


school = School()

student1 = Student("zarah", 14, "address1", "S001", "9th")
student2 = Student("sara", 15, "address2", "S002", "10th")
school.add_student(student1)
school.add_student(student2)

teacher1 = Teacher("sana", 40, "address3", "T001", "Mathematics")
teacher2 = Teacher("ali", 35, "address4", "T002", "Science")
school.add_teacher(teacher1)
school.add_teacher(teacher2)


course1 = Course("Algebra", "MATH101")
course2 = Course("Biology", "SCI201")
school.add_course(course1)
school.add_course(course2)

school.assign_course(teacher1, course1)
school.assign_course(teacher2, course2)


school.enroll_student_in_course(student1, course1)
school.enroll_student_in_course(student2, course2)


print("Students:" ,student1.name,',',student2.name)
print("Teachers:" ,teacher1.name, ',', teacher2.name)
print("Courses:", course1.course_name, ',', course2.course_name )

print(student1.name, "is enrolled in courses:",course2.course_name)
print(teacher1.name, "is assigned courses:",course1.course_name)
print(course2.course_name, "is enrolled students:",student1.name)
