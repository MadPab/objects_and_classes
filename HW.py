class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grade_lecturer:
                lecturer.grade_lecturer[course] += [grade]
            else:
                lecturer.grade_lecturer[course] = [grade]
            return "Оценка добавлена"
        else:
            return 'Ошибка'

    def avg_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        avg_grade = total_grades / total_courses if total_courses > 0 else 0
        return avg_grade

    def __str__(self):
        avg_grade = self.avg_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\n" \
                f"Курсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"
    
    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

    def __ne__(self, other):
        return self.avg_grade() != other.avg_grade()
    
    def avg_grade_by_course(self, students, course):
        relevant_students = [student for student in students if course in student.grades]
        total_grades = sum(sum(student.grades[course]) for student in relevant_students)
        total_students = sum(len(student.grades[course]) for student in relevant_students)

        if total_students > 0:
            return total_grades / total_students
        else:
            return 0    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name} \nФамилия:{self.surname}"
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_lecturer = {}

    def avg_grade(self):
        total_grades = sum(sum(grades) for grades in self.grade_lecturer.values())
        total_courses = sum(len(grades) for grades in self.grade_lecturer.values())
        avg_grade = total_grades / total_courses if total_courses > 0 else 0
        return avg_grade

    def __str__(self):
        avg_grade = self.avg_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.2f}"

    def avg_grade_for_lecturers(self, lecturers, course):
        total_grades = 0
        total_lecturers = 0
        for lecturer in lecturers:
            if course in lecturer.grade_lecturer:
                if lecturer.grade_lecturer[course]:
                    total_grades += sum(lecturer.grade_lecturer[course])
                    total_lecturers += 1

        if total_lecturers > 0:
            return total_grades / total_lecturers
        else:
            return 0      

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return "Оценка добавлена"
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия:{self.surname}"
    

student_1 = Student('Tom', 'Sawyer', 'Male')
student_2 = Student('Marie', 'Curie', 'Female')
student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Java', 'C++']
student_2.finished_courses += ['Введение в программирование']
student_1.grades = {'Python': [9, 8, 10], 'Git': [10, 9, 10]}
student_2.grades = {'Python': [8, 7, 10], 'Git': [9, 10, 6]}
print(student_1)
print(student_2)
print(student_1 == student_2)
print(student_1 < student_2)
print(student_1 > student_2)
print(student_1 >= student_2)
print(student_1 <= student_2)
print(student_1 != student_2)



mentor_1 = Mentor('Adam', 'Jensen')
mentor_2 = Mentor('Emma', 'Adams')
print(mentor_1)
print(mentor_2)


lecturer_1 = Lecturer('Albert', 'Einstein')
lecturer_2 = Lecturer('Robert', 'Oppenheimer')
lecturer_1.grade_lecturer = {'Python': [10, 9, 9, 10, 9]}
lecturer_2.grade_lecturer = {'Python': [10, 10, 8, 8, 9]}
print(f'Lecturer: \n{lecturer_1}')
print(f'Lecturer: \n{lecturer_2}')


reviewer_1 = Reviewer('Isaac', 'Asimov')
reviewer_2 = Reviewer('John', 'Doe')
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_2.rate_hw(student_1, "Python", 8)
reviewer_2.rate_hw(student_2, "Введение в программирование", 10)
print(reviewer_1)
print(reviewer_2)

print(student_1.rate_lecturer(lecturer_1, "Python", 10))
