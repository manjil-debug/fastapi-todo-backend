from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, todo as crud
from app.database import SessionLocal
from app.deps import get_current_active_user

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.TodoOut)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    return crud.create_todo(db=db, todo=todo, owner_id=current_user.id)


@router.get("/", response_model=List[schemas.TodoOut])
def list_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    todos = crud.get_todos(db, skip=skip, limit=limit, user_id=current_user.id)
    return todos


@router.get("/{todo_id}", response_model=schemas.TodoOut)
def get_todo(todo_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    todo = crud.get_todo(db, todo_id=todo_id, user_id=current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.put("/{todo_id}", response_model=schemas.TodoOut)
def update_todo(todo_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    updated_todo = crud.update_todo(db, todo_id=todo_id, todo=todo, user_id=current_user.id)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    deleted_todo = crud.delete_todo(db, todo_id=todo_id, user_id=current_user.id)
    if not deleted_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"detail": "Todo deleted successfully"}


@router.put("/{todo_id}/status", response_model=schemas.TodoOut)
def update_todo_status(todo_id: int, completed: bool, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    updated_todo = crud.update_todo_status(db, todo_id=todo_id, completed=completed, user_id=current_user.id)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo