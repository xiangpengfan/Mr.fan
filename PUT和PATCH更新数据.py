'''
更新数据分为两种：完全替换原始数据PUT和部分替换原始数据PATCH

实际应用中，部分团队或者项目只用PUT更新数据，即使是更新部分数据

但我们应该知道PUT和PATCH的区别
'''

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app=FastAPI()

class Item(BaseModel):
    name:str|None=None
    description:str|None=None
    price:float|None=None
    tax:float=10.5
    tags:list[str]=[]

items={
    'foo':{
        'name':'Foo',
        'price':56.1
    },
    'bar':{
        'name':'Bar',
        'description':'The Bar Wrestler',
        'price':62,
        'tax':20
    },
    'baz':{
        'name':'Baz',
        'description':None,
        'price':50,
        'tax':10.5,
        'tags':['baz']
    }
}

@app.get('/items/{item_id}',response_model=Item,
         description='更新完成后点这里获取数据 ',
        tags=['获取数据']
         )
async def read_item(item_id:str):
    return items[item_id]

@app.put('/items/{item_id}',
         response_model=Item,
         tags=['更新替换全部内容']
         )
async def update_item(item_id:str,item:Item):
    items[item_id]=jsonable_encoder(item)
    #jsonable_encoder,将各种形式转换成json格式
    return items[item_id]

@app.patch('/items2/{item_id}',
           response_model=Item,
           tags=['更新部分数据']
           )
async def update_item2(item_id:str,item:Item):
    stored_item=items[item_id]
    stored_item_model=Item(**stored_item)
    update_data=item.model_dump(exclude_unset=True)
    #model_dump，将pydantic模型转换成字典，用来打散模型
    updated_item=stored_item_model.model_copy(update=update_data)
    #model_copy，基于已存储的旧数据，创建新模型实例，并用 update_data 覆盖指定字段。
    items[item_id]=jsonable_encoder(updated_item)
    #将处理好的模型放入字典
    return items[item_id]