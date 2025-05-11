from sqlalchemy import Column, Integer, String
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    completed = Column(Integer, default=0)  # 0 pour non terminé, 1 pour terminé
