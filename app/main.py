from fastapi import FastAPI
from app.routers import todo ,user, auth

app = FastAPI(title="FastAPI Docker Test")

app.include_router(todo.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI Docker is running successfully!"}
