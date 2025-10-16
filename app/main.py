from fastapi import FastAPI
from app.routers import todo

app = FastAPI(title="FastAPI Docker Test")

app.include_router(todo.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI Docker is running successfully!"}
