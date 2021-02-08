from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user_name: str
    user_id: int
    Description: Optional[bool] = None

@app.get("/")
def read_root():
    return "규빈 "+  "World"

@app.get("/users/{user_id}")
def read_user(user_id: int,user_name: str,q: Optional[str] = None):
    return {"user_id": user_id, "user_name" : user_name, "q": q}

@app.put("/users/{user_id}")
def update_user(user_id: int, user_name : str, user: User):
    return {"user_id": user.user_id, "user_id": user_id, "user_name": user.user_name, "user_name": user_name}

