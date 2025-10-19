from fastapi import FastAPI
from app.routers import todo ,user, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI Docker Test")

origins = [
    "http://localhost:3000",   # React local dev
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)

app.include_router(todo.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI Docker is running successfully!"}
