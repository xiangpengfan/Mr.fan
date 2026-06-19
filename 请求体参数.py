'''
请求体参数可以从请求体中获取数据
'''




from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None


app=FastAPI()

# @app.post('/items')
# async def create_item(item:Item):
#     #继承了BaseModel子类的参数，可以直接捕获前端的同名参数
#     return item

@app.post('/items/{item_id}')
async def create_item(item_id:int,item:Item,q:str|None=None):
    item_dict=item.model_dump()
    if item.tax is not None:
        total_price=item.price+item.tax
        item_dict.update({'total_price':total_price})
        item_dict.update({'受欢迎指数':item_id})
        item_dict.update({'q是随便加上的查询参数':q})
    return item_dict