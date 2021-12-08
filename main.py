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

    def add_marks(self, course, grade):
        if course in self.grades:
            self.grades[course] += [grade]
        else:
            self.grades[course] = [grade]

    def average_grade_for_h_w(self):
        list_all_grades = []
        for course in self.grades:
            list_all_grades += self.grades[course]
        self.avg = sum(list_all_grades) / len(list_all_grades)
        return self.avg

    def courses_in_progress(self):
        return self.courses_in_progress

    def finished_courses(self):
        return self.finished_courses

    def __str__(self):
        first_name = "Name: {}".format(self.name)
        last_name = "Surname: {}".format(self.surname)
        avg = "Average grade for homeworks: {}".format(self.avg)
        courses_in_progress = "Courses in the progress of studying: {}".format(self.courses_in_progress)
        finished_courses = "Finished courses: {}".format(self.finished_courses)
        return "{}\n{}\n{}\n{}\n{}".format(first_name, last_name, avg, courses_in_progress, finished_courses)

    def __lt__(self, other):
        return other.avg < self.avg


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.avg = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'error'

    def __str__(self):
        first_name = "Name: {}".format(self.name)
        last_name = "Surname: {}".format(self.surname)
        return "{}\n{}\n".format(first_name, last_name)


class Lector(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.avg = {}

    def add_marks(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'error'

    def average_grade_for_lectures(self):
        list_all_grades = []
        for course in self.grades:
            list_all_grades += self.grades[course]
        self.avg = sum(list_all_grades) / len(list_all_grades)
        return self.avg

    def __str__(self):
        first_name = "Name: {}".format(self.name)
        last_name = "Surname: {}".format(self.surname)
        avg = "Average grade for lectures: {}".format(self.average_grade_for_lectures())
        return "{}\n{}\n{}".format(first_name, last_name, avg)


best_student = Student('Ruoy', 'Eman', 'woman')
best_student.add_marks('Python', 7)
best_student.add_marks('Python', 9)
best_student.add_marks('Python', 9)
best_student.add_marks('Git', 3)
best_student.add_marks('Git', 5)
best_student.add_marks('Git', 6)
best_student.average_grade_for_h_w()
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Introduction to programming']
print(best_student)
print("\n")


cool_reviewer = Reviewer('Some', 'Buddy')
print("#Cool reviewer#")
print(cool_reviewer)
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
cool_lector.add_marks(second_student, 'Algoritmika1', 7)
cool_lector.add_marks(second_student, 'Algoritmika2', 9)
cool_lector.add_marks(second_student, 'Algoritmika3', 5)
cool_lector.average_grade_for_lectures()
print(cool_lector)

# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции
# и студентов по средней оценке за домашние задания.
print(best_student > cool_lector)

