from fastapi import FastAPI
from .routers import items, users
from .database import engine
from . import models

app = FastAPI()

# データベースに不足しているテーブルを自動作成する
models.Base.metadata.create_all(bind=engine)

# ルーターを追加
app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
