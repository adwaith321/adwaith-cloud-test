from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

student_class = Table(
    "student_class",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("class_id", Integer, ForeignKey("classes.id"))
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    age = Column(Integer)
    city = Column(String)
    classes = relationship("Class", secondary=student_class, back_populates="students")

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String)
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    number_of_hours = Column(Integer)
    students = relationship("Student", secondary=student_class, back_populates="classes")
