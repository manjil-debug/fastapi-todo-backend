from fastapi import FastAPI

app = FastAPI(title="FastAPI Docker Test")

@app.get("/")
def read_root():
    return {"message": "FastAPI Docker is running successfully!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
