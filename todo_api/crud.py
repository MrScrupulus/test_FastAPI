# crud.py
from sqlalchemy.orm import Session
from . import models, schema

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: schema.TodoCreate):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, completed: bool):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo:
        todo.completed = completed
        db.commit()
        db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return todo
