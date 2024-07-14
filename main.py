class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def __str__(self):
        info = (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
        return info

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

        return 'Ошибка'

    def average_grade(self):
        total = []
        for value in self.grades.values():
            total += value
        if total:
            average = sum(total) / len(total)
            return round(average, 1)

        return 'Нет оценки'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        info = (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")
        return info


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        info = (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade()}\n")
        return info

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def average_grade(self):
        total = []
        for value in self.grades.values():
            total += value
        if total:
            average = sum(total) / len(total)
            return round(average, 1)

        return 'Нет оценки'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

        return 'Ошибка'


def students_average_grade(students_list, course):
    total = []
    for student in students_list:
        if course in student.courses_in_progress:
            value = student.average_grade()
            total.append(value)
    if total:
        average = sum(total) / len(total)
        return round(average, 1)

    return 'Нет оценки'


def lecturers_average_grade(lecturers_list, course):
    total = []
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            value = lecturer.average_grade()
            total.append(value)
    if total:
        average = sum(total) / len(total)
        return round(average, 1)

    return 'Нет оценки'


student_one = Student('Mickie', 'Mouse', 'Animal')
student_two = Student('Muffin', 'Man', 'Male')
mentor_one = Mentor('Super', 'Man')
mentor_two = Mentor('Super', 'Girl')
lecturer_one = Lecturer('Obi', 'Wan')
lecturer_two = Lecturer('Anakin', 'Skywalker')
reviewer_one = Reviewer('Master', 'Yoda')
reviewer_two = Reviewer('Cookie', 'Monster')

student_one.courses_in_progress += ['Python', 'Git']
student_one.finished_courses += ['Дрессировка котов']
student_two.courses_in_progress += ['Python']
student_two.finished_courses += ['Шеф-повар за три часа']
mentor_one.courses_attached += ['Python']
mentor_two.courses_attached += ['Python']
lecturer_one.courses_attached += ['Python']
lecturer_two.courses_attached += ['Python']
reviewer_one.courses_attached += ['Python']
reviewer_two.courses_attached += ['Python']

student_one.rate_lecturer(lecturer_one, 'Python', 10)
student_one.rate_lecturer(lecturer_one, 'Python', 9)
student_one.rate_lecturer(lecturer_one, 'Python', 9)

student_two.rate_lecturer(lecturer_two, 'Python', 6)
student_two.rate_lecturer(lecturer_two, 'Python', 6)
student_two.rate_lecturer(lecturer_two, 'Python', 6)

reviewer_one.rate_hw(student_one, 'Python', 10)
reviewer_one.rate_hw(student_one, 'Python', 10)
reviewer_one.rate_hw(student_one, 'Python', 10)

reviewer_two.rate_hw(student_two, 'Python', 10)
reviewer_two.rate_hw(student_two, 'Python', 10)
reviewer_two.rate_hw(student_two, 'Python', 10)

print(student_one)
print(student_two)
print(mentor_one)
print(mentor_two)
print(lecturer_one)
print(lecturer_two)
print(reviewer_one)
print(reviewer_two)

print(f"Равны ли средние оценки студентов за домашние задания: {student_one == student_two}")
print(f"Равны ли средние оценки лекторов за лекции: {lecturer_one == lecturer_two}")

student_list = [student_one, student_two]
students_average = students_average_grade(student_list, 'Python')
print(f"Cредняя оценка за домашние задания по всем студентам: {students_average}")

lecturer_list = [lecturer_one, lecturer_two]
lecturers_average = lecturers_average_grade(lecturer_list, 'Python')
print(f"Cредняя оценка за лекции всех лекторов: {lecturers_average}")
