# schema.py
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    completed: bool

class TodoOut(TodoBase):
    id: int
    completed: bool

    class Config:
        from_attributes = True
