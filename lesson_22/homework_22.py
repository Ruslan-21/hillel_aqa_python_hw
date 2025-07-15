from sqlalchemy import Column, Integer, String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.db.tables.orm_students import Base, Students, Course

psql_conn_str = "postgresql://postgres:test_password@localhost:5432/postgres"

engine = create_engine(psql_conn_str)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def create_courses(session):
    course_names = ['QA', 'AQA', 'Python', 'PHP', 'JS']
    courses = [Course(name_course=n) for n in course_names]
    session.add_all(courses)
    session.commit()
    return courses

def create_students(session, courses):
    for i in range(1, 21):
        student = Students(name=f"Student{i}")

        student.courses.append(courses[i % len(courses)])
        session.add(student)
    session.commit()



def add_student(session, name, course_name):
    course = session.query(Course).filter_by(name_course=course_name).first()
    if not course:
        print(f"Курс {course_name} не знайдено")
        return
    student = Students(name=name)
    student.courses.append(course)
    session.add(student)
    session.commit()
    print(f"Додавання студента: {name} на курс {course_name}")

def print_students_in_course(session, course_name):
    course = session.query(Course).filter_by(name_course=course_name).first()
    if not course:
        print(f"Курс {course_name} не знайдено")
        return
    print(f"Студенти на курсі {course_name}:")
    for student in course.students:
        print(student.name)

def update_student_name(session, old_name, new_name):
    student = session.query(Students).filter_by(name=old_name).first()
    if not student:
        print(f"Студента {old_name} не знайдено")
        return
    student.name = new_name
    session.commit()
    print(f"Ім`я оновленого студента: {old_name} на {new_name}")



def delete_student(session, student_name):
    student = session.query(Students).filter_by(name=student_name).first()
    if not student:
        print(f"Студента {student_name} не знайдено")
        return
    session.delete(student)
    session.commit()
    print(f"Студент {student_name} видалений")



courses = create_courses(session)
create_students(session, courses)

add_student(session, 'Student1', 'AQA')
print_students_in_course(session, 'AQA')
update_student_name(session, 'Student1', 'Student2')
delete_student(session, 'Student2')


