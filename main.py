class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def assigning_marks(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_attached:
            lector.add_marks(self, course, grade)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'error'


class Lector(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def add_marks(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'error'


best_student = Student('Ruoy', 'Eman', 'woman')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 4)
print(best_student.grades)

second_student = Student('Lola', 'Frimey', 'woman')
second_student.courses_in_progress += ['Algoritmika']

cool_lector = Lector('Denis', 'Kyzin')
cool_lector.courses_attached += ['Algoritmika']
cool_lector.add_marks(second_student, 'Algoritmika', 7)
cool_lector.add_marks(second_student, 'Algoritmika', 9)
cool_lector.add_marks(second_student, 'Algoritmika', 5)
print(cool_lector.grades)


