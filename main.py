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


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached:
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

    def average_mark_for_lecture_all_lector_within_course(self, course):
        pass


best_student = Student('Ruoy', 'Eman', 'woman')
best_student.add_marks('Python', 9)
best_student.add_marks('Python', 9)
best_student.add_marks('Python', 9)
best_student.add_marks('Python for advanced', 3)
best_student.add_marks('Python for advanced', 5)
best_student.add_marks('Python for advanced', 6)
best_student.average_grade_for_h_w()
best_student.courses_in_progress += ['Python', 'Python for advanced']
best_student.finished_courses += ['Introduction to programming']
print(best_student)
print("\n")

first_student = Student('Nikita', 'Gordon', 'man')
first_student.add_marks('Python', 5)
first_student.add_marks('Python', 6)
first_student.add_marks('Python', 8)
first_student.add_marks('C++', 6)
first_student.add_marks('C++', 5)
first_student.add_marks('C++', 4)
first_student.average_grade_for_h_w()
first_student.courses_in_progress += ['Python', 'C++']
first_student.finished_courses += ['How to find good work']
print(first_student)
print("\n")


third_student = Student('Liza', 'Vornitsa', 'woman')
third_student.add_marks('JS', 6)
third_student.add_marks('JS', 5)
third_student.add_marks('JS', 4)
third_student.add_marks('Python', 5)
third_student.add_marks('Python', 6)
third_student.add_marks('Python', 8)
third_student.average_grade_for_h_w()
third_student.courses_in_progress += ['JS', 'Python']
third_student.finished_courses += ["Introduction to Python"]
print(third_student)
print("\n")

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Python for advanced']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'Python for advanced', 10)
cool_reviewer.rate_hw(best_student, 'Python for advanced', 8)
cool_reviewer.rate_hw(best_student, 'Python for advanced', 4)
print(best_student.grades)
print(cool_reviewer)

first_reviewer = Reviewer('Hannah', 'Curni')
first_reviewer.courses_attached += ['Python', 'C++']
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 8)
first_reviewer.rate_hw(first_student, 'Python', 4)
first_reviewer.rate_hw(first_student, 'C++', 10)
first_reviewer.rate_hw(first_student, 'C++', 8)
first_reviewer.rate_hw(first_student, 'C++', 4)
print(first_student.grades)
print(first_reviewer)

second_reviewer = Reviewer('Yulia', 'Yaroslava')
second_reviewer.courses_attached += ['JS']
second_reviewer.rate_hw(third_student, 'JS', 10)
second_reviewer.rate_hw(third_student, 'JS', 8)
second_reviewer.rate_hw(third_student, 'JS', 4)
print(third_student.grades)
print(second_reviewer)


cool_lector = Lector('Denis', 'Kyzin')
cool_lector.courses_attached += ['Python', 'Python for advanced']
cool_lector.add_marks(best_student, 'Python', 7)
cool_lector.add_marks(best_student, 'Python', 9)
cool_lector.add_marks(best_student, 'Python', 5)
cool_lector.add_marks(best_student, 'Python for advanced', 7)
cool_lector.add_marks(best_student, 'Python for advanced', 9)
cool_lector.add_marks(best_student, 'Python for advanced', 5)
cool_lector.average_grade_for_lectures()
print(cool_lector)
print("\n")

first_lector = Lector('Andrey', 'Efrimov')
first_lector.courses_attached += ['Python', 'C++']
first_lector.add_marks(first_student, 'Python', 7)
first_lector.add_marks(first_student, 'Python', 9)
first_lector.add_marks(first_student, 'Python', 5)
first_lector.add_marks(first_student, 'C++', 7)
first_lector.add_marks(first_student, 'C++', 9)
first_lector.add_marks(first_student, 'C++', 5)
first_lector.average_grade_for_lectures()
print(first_lector)
print("\n")

second_lector = Lector('Olga', 'Svirnova')
second_lector.courses_attached += ['JS', 'Python']
second_lector.add_marks(third_student, 'JS', 2)
second_lector.add_marks(third_student, 'JS', 4)
second_lector.add_marks(third_student, 'JS', 3)
second_lector.add_marks(third_student, 'Python', 9)
second_lector.add_marks(third_student, 'Python', 8)
second_lector.add_marks(third_student, 'Python', 9)
second_lector.average_grade_for_lectures()
print(second_lector)

#to compare student and lector
print(best_student > cool_lector)


def average_mark_by_students_within_course(list_students, course):
    marks_by_course = []
    for student in list_students:
        marks_by_course += student.grades.get(course, [])
    return sum(marks_by_course) / len(marks_by_course)


print('\nAvg mark {} by course {} of all student'.format(average_mark_by_students_within_course([best_student, first_student, third_student], 'Python'), 'Python'))


def average_mark_by_lectors_for_lectures_within_course(list_lectors, course):
    marks_by_lectures = []
    for lector in list_lectors:
        marks_by_lectures += lector.grades.get(course, [])
    return sum(marks_by_lectures) / len(marks_by_lectures)

print('\nAvg mark {} by course {} of all lectures by lectors'.format(average_mark_by_lectors_for_lectures_within_course([cool_lector, first_lector, second_lector], 'Python'), 'Python'))
