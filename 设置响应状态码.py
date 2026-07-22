'''
通过JSONResponse设置响应状态码
'''

from typing import Annotated
from fastapi import FastAPI, status,Body
from fastapi.responses import JSONResponse

app=FastAPI()

items={
    "foo":{"name":"Foo","price":56.2},
    "bar":{"name":"Bar","price":74.2},
}

@app.put("/item/{item_id}")
async def update_item(
    item_id: str,
    name: Annotated[str, Body()]=None,
    price: Annotated[float, Body()]=None,
):
    if item_id in items:
        item=items[item_id]
        item["name"]=name
        item["price"]=price
        return item
    else:
        item={"name":name,"price":price}
        items[item_id]=item
        return JSONResponse(status_code=201,content={"message":f"添加成功{item_id}"})
