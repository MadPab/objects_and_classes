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
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades)
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\n" \
                f"Курсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"
    
    def __eq__(self, other):
        return self.avg_grade == other.avg_grade

    def __lt__(self, other):
        return self.avg_grade < other.avg_grade

    def __le__(self, other):
        return self.avg_grade <= other.avg_grade

    def __gt__(self, other):
        return self.avg_grade > other.avg_grade

    def __ge__(self, other):
        return self.avg_grade >= other.avg_grade

    def __ne__(self, other):
        return self.avg_grade != other.avg_grade
    
    def avg_grade_by_course(self, students, course):
        total_grades = 0
        total_students = 0
        for student in students:
            if course in student.grades:
                if student.grades[course]:
                    total_grades += sum(student.grades[course])
                    total_students += len(student.grades[course])

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
        avg_grade = sum(sum(grades) / len(grades) for grades in self.grade_lecturer.values()) / len(self.grade_lecturer)
        return avg_grade

    def __str__(self):
        avg_grade = self.avg_grade()
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {avg_grade}"
    
    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade

    def __ne__(self, other):
        return self.avg_grade() != other.avg_grade
    
    def avg_grade_for_lecturers(lecturers, course):
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
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name} \nФамилия:{self.surname}"
    
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.grades = {'Python': [9, 8, 10], 'Git': [10, 9, 10]}
print(f'Student: \n{best_student}')

cool_mentor = Mentor('Isaac', 'Asimov')
print(f'Mentor: \n{cool_mentor}')

 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
print(f'Reviewer: \n{cool_reviewer}')
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)

python_lecturer = Lecturer('John', 'Doe')
python_lecturer.grade_lecturer = {'Python': [10, 9, 9, 9, 9]}
print(f'Lecturer: \n{python_lecturer}')

# best_student.rate_lecturer(python_lecturer, 'Python', 9)
# print(f"{python_lecturer.name} {python_lecturer.surname} - {python_lecturer.grade_lecturer}")

