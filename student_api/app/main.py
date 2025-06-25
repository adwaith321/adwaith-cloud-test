from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.put("/students/{student_id}")
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.update_student(db, student_id, student)

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_id)

@app.post("/classes/", response_model=schemas.Class)
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.create_class(db, class_)

@app.put("/classes/{class_id}")
def update_class(class_id: int, class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    return crud.update_class(db, class_id, class_)

@app.delete("/classes/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    return crud.delete_class(db, class_id)

@app.post("/register/")
def register_student(student_id: int, class_id: int, db: Session = Depends(get_db)):
    success = crud.register_student_to_class(db, student_id, class_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student or Class not found")
    return {"message": "Student registered to class"}

@app.get("/classes/{class_id}/students", response_model=list[schemas.Student])
def get_registered_students(class_id: int, db: Session = Depends(get_db)):
    return crud.get_students_for_class(db, class_id)
