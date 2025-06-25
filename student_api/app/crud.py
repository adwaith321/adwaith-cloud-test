from sqlalchemy.orm import Session
from . import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).get(student_id)
    if db_student:
        for key, value in student.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).get(student_id)
    if student:
        db.delete(student)
        db.commit()
    return student

def create_class(db: Session, class_: schemas.ClassCreate):
    db_class = models.Class(**class_.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def update_class(db: Session, class_id: int, class_: schemas.ClassCreate):
    db_class = db.query(models.Class).get(class_id)
    if db_class:
        for key, value in class_.dict().items():
            setattr(db_class, key, value)
        db.commit()
        db.refresh(db_class)
    return db_class

def delete_class(db: Session, class_id: int):
    db_class = db.query(models.Class).get(class_id)
    if db_class:
        db.delete(db_class)
        db.commit()
    return db_class

def register_student_to_class(db: Session, student_id: int, class_id: int):
    student = db.query(models.Student).get(student_id)
    class_ = db.query(models.Class).get(class_id)
    if student and class_:
        student.classes.append(class_)
        db.commit()
        return True
    return False

def get_students_for_class(db: Session, class_id: int):
    class_ = db.query(models.Class).get(class_id)
    return class_.students if class_ else []
