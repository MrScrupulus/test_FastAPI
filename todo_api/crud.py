from sqlalchemy.orm import Session
from models import Todo

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()

def create_todo(db: Session, task: str):
    db_todo = Todo(task=task)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
