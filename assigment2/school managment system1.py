# Base class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Student class
class Student(Person):
    def __init__(self, name, age, address, student_id, grade):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grade = grade
        self.enrolled_courses = []

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)
        course.enrolled_students.append(self)

# Teacher class
class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)

# Course class
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.enrolled_students = []

# School class
class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)
        print(self.students)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(self.teachers)

    def add_course(self, course):
        self.courses.append(course)
        print(self.courses)

    def assign_course_to_teacher(self, teacher, course):
        teacher.assign_course(course)

    def enroll_student_in_course(self, student, course):
        student.enroll_in_course(course)

# Example usage:
school = School()
student1 = Student("Alice", 14, "123 Main St", "S001", "9th Grade")
student2 = Student("Bob", 15, "456 Elm St", "S002", "10th Grade")

teacher1 = Teacher("Mr. Smith", 40, "789 Oak St", "T001", "Mathematics")
teacher2 = Teacher("Ms. Johnson", 35, "101 Maple St", "T002", "Science")

course1 = Course("Algebra", "MATH101")
course2 = Course("Biology", "SCI101")

school.add_student(student1)
school.add_student(student2)

school.add_teacher(teacher1)
school.add_teacher(teacher2)

school.add_course(course1)
school.add_course(course2)


print(school.assign_course_to_teacher(teacher1, course1))
print(school.assign_course_to_teacher(teacher2, course2))

print(school.enroll_student_in_course(student1, course1))
print(school.enroll_student_in_course(student2, course2))

print(f"{student1.name}'s enrolled courses: {[course.course_name for course in student1.enrolled_courses]}")

print(f"{teacher1.name}'s assigned courses: {[course.course_name for course in teacher1.assigned_courses]}")
