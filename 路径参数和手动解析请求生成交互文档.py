'''
一些新的路由参数和自定义openapi.json----文档生成说明书
'''

import yaml
from fastapi import FastAPI,Request,HTTPException
#from fastapi.routing import APIRouter
from pydantic import BaseModel,ValidationError

# def custom_generate_unique_id(router:APIRouter)->str:
#     #这个函数有且只有一个参数APIRouter
#     return router.name

# app=FastAPI(generate_unique_id=custom_generate_unique_id)

# @app.get("/items/",tags=["items"],openapi_extra={"x-aperture-labs-portal": "blue"})
# async def read_items():
#     """
#     Create an item with all the information:

#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     \f
#     :param item: User input.
#     """
#     return [{"hello":"world"}]

# @app.get("/users/",include_in_schema=False)
# async def read_users():
#     return "你应该看不到这个"


app=FastAPI()

class Item(BaseModel):
    name: str
    tags: list[str]

@app.post(
    "/items/",
    openapi_extra={
        "requestBody": {
            "content": {"application/x-yaml": {"schema": Item.model_json_schema()}},
        },
    },
)
#下面这个函数负责将yaml转换成pydantic模型
async def create_item(request: Request):
    raw_body=await request.body()
    try:
        data=yaml.safe_load(raw_body)
    except yaml.YAMLError as e:
        raise HTTPException(status_code=400,detail=str(e))
    try:
        item=Item.model_validate(data)
    except ValidationError as e:
        raise HTTPException(status_code=400,detail=str(e))
    return item