from fastapi import FastAPI
from .routers import users, items
from .database import engine
from . import models

# # データベースのテーブルを作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/test")
async def root():
    return {"message": "test"}

@app.get("/test2")
async def root():
    return {"message": "test2"}

# # ルータを追加
app.include_router(users.router)
app.include_router(items.router)
