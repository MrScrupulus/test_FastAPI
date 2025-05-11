from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import get_todos, create_todo
from schema import Todo, TodoCreate
from database import SessionLocal

router = APIRouter()

# Dépendance pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/todos", response_model=list[Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = get_todos(db=db, skip=skip, limit=limit)
    return todos

@router.post("/todos", response_model=Todo)
def create_todo_item(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = create_todo(db=db, task=todo.task)
    return db_todo
