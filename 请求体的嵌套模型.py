from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl

# app = FastAPI()

# class Item(BaseModel):
#     name:str
#     description:str|None=None
#     price:float
#     tax:float|None=None
#     tags:set[str]=set()

# @app.put('/items/{item_id}')
# async def update_item(item_id:int,item:Item):
#     results={'item_id':item_id,'item':item}
#     return results


app=FastAPI()

class Image(BaseModel):
    url:HttpUrl
    name:str

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None
    tags:set[str]=set()
    image:list[Image]|None=None
#当一些信息特别重要时，单数据无法描述，就嵌套一个BaseModel子类，多维展开这个数据，这就会使数据更加的立体

class Offer(BaseModel):
    name:str
    description:str|None=None
    price:float
    items:list[Item]

@app.put('/items/{iten_id}')
async def update_item(item_id:int,item:Offer):
    results={'item_id':item_id,'item':Offer}
    return results
