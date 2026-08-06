"""
如果响应和函数是独立的,
那么可以提前关闭函数，可以数据库连接
"""


import time
from typing import Annotated
from fastapi import FastAPI,Depends,HTTPException
from fastapi.responses import StreamingResponse
from sqlmodel import Session,Field,SQLModel,create_engine

engine=create_engine("postgresql://postgres:258456@localhost:5432/test")

class User(SQLModel,table=True):
    id:int|None=Field(default=None,primary_key=True)
    name:str
    
SQLModel.metadata.create_all(engine)

app=FastAPI()

def get_session():
    with Session(engine) as session:
        yield session

def get_user(user_id:int,session:Annotated[Session,Depends(get_session)]):
    user=session.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")

def generate_stream(query:str):
    for ch in query:
        yield ch
        time.sleep(0.1)

@app.get("/generate",dependencies=[Depends(get_user)])
def generate(query:str):
    
    return StreamingResponse(content=generate_stream(query))