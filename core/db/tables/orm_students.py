from sqlalchemy import Column, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker



Base = declarative_base()

enrollments = Table(
    "enrollments",
    Base.metadata,
    Column('students_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=enrollments, back_populates="students")


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name_course = Column(String)
    students = relationship("Students", secondary=enrollments, back_populates="courses")



