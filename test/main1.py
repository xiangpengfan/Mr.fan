'''
测试主要是为了确保代码功能的实现，和对整体没有影响
通常写完代码开发人员要进行小测试，来保证代码可以正常运行，
然后再交由专业的测试人员对代码融入系统后的整个系统性进行测试
'''

# from fastapi import FastAPI
# from fastapi.testclient import TestClient

# app=FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "你自主学习能力极强，主动探索不断精进"}


# def test_read_main():
#     with TestClient(app) as client:
#         response=client.get("/")
#         assert response.status_code==200
#         assert response.json()=={"message":"你自主学习能力极强，主动探索不断精进"}
#         print("测试通过")

# if __name__=="__main__":
#     test_read_main()

from typing import Annotated

from fastapi import FastAPI,Header,HTTPException
from pydantic import BaseModel

fake_secret_key="1111"

fake_db={
    "foo":{"id":"foo","title":"Foo","description":"这是第一条数据"},
    "bar":{"id":"bar","title":"Bar","description":"这是第二条数据"},
}

app=FastAPI()

class Item(BaseModel):
    id:str
    title:str
    description:str|None=None

@app.get("/items/{item_id}",response_model=Item)
async def read_item(item_id:str,X_token:Annotated[str,Header()]):
    if item_id not in fake_db:
        raise HTTPException(status_code=404,detail="没找到该数据")
    if X_token!=fake_secret_key:
        raise HTTPException(status_code=400,detail="没有权限")
    return fake_db[item_id]

@app.post("/items/")
async def creat_item(item:Item,X_token:Annotated[str,Header()])->Item:
    if X_token!=fake_secret_key:
        raise HTTPException(status_code=400,detail="没有权限")
    if item.id in fake_db:
        raise HTTPException(status_code=400,detail="id已存在")
    fake_db[item.id]=item.model_dump()
    return item