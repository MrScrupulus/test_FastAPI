# routers/todo.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schema import TodoCreate, TodoUpdate, TodoOut
import crud

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=list[TodoOut])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@router.post("/", response_model=TodoOut)
def add_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@router.put("/{todo_id}", response_model=TodoOut)
def mark_todo(todo_id: int, update: TodoUpdate, db: Session = Depends(get_db)):
    updated = crud.update_todo(db, todo_id, update.completed)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@router.delete("/{todo_id}", status_code=204)
def remove_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
