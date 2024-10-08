from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database

app = FastAPI()

# DB初期化
models.Base.metadata.create_all(bind=database.engine)

# データ取得エンドポイント
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items

# データ作成エンドポイント
@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(database.get_db)):
    db_item = models.Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
