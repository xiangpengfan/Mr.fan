from typing import Annotated
from fastapi import FastAPI,Path,Body
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):   #创建一个请求体参数，从请求体中获取数据
    name:str
    description:str|None=None
    price:float
    tax:float|None=None

class User(BaseModel):
    username:str
    full_name:str|None=None

@app.post('/items/{item_id}')
async def update_item(
    item_id:Annotated[int,Path(title="获得item_id",gt=0,le=1000)],#路径参数
    item2:Annotated[str,Body(embed=True)],
    q:str|None=None,          #查询参数
    item:Item|None=None,     #请求体参数
    user:User|None=None       #第二个请求体参数
    ):
    results={'item_id':item_id}
    if q:
        results.update({'q':q})
    if item:
        results.update({'item':item})
    return results
