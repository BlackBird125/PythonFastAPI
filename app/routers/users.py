from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# ユーザー取得エンドポイント
@router.get("/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# ユーザー作成エンドポイント
@router.post("/")
def create_user(name: str, email: str, db: Session = Depends(database.get_db)):
    db_user = models.User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
