from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models, database

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.get("/")
def read_items(db: Session = Depends(database.get_db)):
    return db.query(models.Item).all()

@router.post("/")
def create_item(name: str, description: str, db: Session = Depends(database.get_db)):
    item = models.Item(name=name, description=description)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
