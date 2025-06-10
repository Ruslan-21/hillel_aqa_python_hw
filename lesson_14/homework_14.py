class Student:




    def student_list(self, name, surname, age, grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.grade = grade


    def grade_students(self, grade):
        self.grade = grade






    def info_students(self):
        print(f'Ім`я: {self.name}')
        print(f'Прізвище: {self.surname}')
        print(f'Вік: {self.age}')
        print(f'Средній бал: {self.grade}')

student1 = Student()
student1.student_list('Alex', 'Smith', '18', '10.5')


print(f'Інформація про студента:')
student1.info_students()

student1.grade_students(11.8,)


print(f'Оновлена інформація про студента:')
student1.info_students()

