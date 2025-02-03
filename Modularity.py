class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student):
        if student not in self.students:
            student.set_id(len(self.students) + 1)
            self.students.append(student)

    def add_student_grade(self, student, course, grade: int):
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self):
        return self.students

    def get_courses(self):
        return self.courses

    def get_students_ordered_by_average_grade(self):
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)


"""Student class with student name and grades."""



class Student:
    def __init__(self, name: str):
        self.name = name
        self.id = None
        self.grades = []

    def set_id(self, id: int):
        if self.id is None:
            self.id = id

    def get_id(self):
        return self.id

    def get_grades(self):
        return self.grades

    def add_grade(self, course, grade: int):
        self.grades.append((course, grade))

    def get_average_grade(self):
        if not self.grades:
            return -1
        return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        return self.name
    
    
    
"""Course class with name and grades."""

class Course:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, student, grade: int):
        self.grades.append((student, grade))

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        if not self.grades:
            return -1
        return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        return self.name
