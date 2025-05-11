
from fastapi import FastAPI
from database import Base, engine
from routers import todo

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(todo.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API Todo!"}