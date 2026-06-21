from typing import Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel,Field

app=FastAPI()

class Item(BaseModel):
    name: str
    description: str | None=Field(
        default=None,
        title='这个是请求体参数的一个属性',
        max_length=300
    )
    price: float=Field(
        gt=0,
        description='价格必须大于0'
    )
    tax: float | None = None

@app.put('/item/{item_id}')
async def update_item(item_id:int,item:Item=Body(embed=True)):
    results={'item_id':item_id,'item':item}
    return results

