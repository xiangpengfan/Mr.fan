from fastapi import FastAPI,Query,Body
from pydantic import BaseModel,Field
from typing import Annotated

app=FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None #Field(default=None, example='A very nice 数据')
    price:float
    tax:float=None

    # model_config={
    #     'json_schema_extra':{
    #         'examples':[
    #             {
    #                 'name':'Foo',
    #                 'description':'A very nice Item',
    #                 'price':35.4,
    #                 'tax':3.2
    #             }
    #         ]
    #     }
    #}

# @app.put('/items/{item_id}')
# async def update_item(item_id:int,
# item:Annotated[Item,
# Body(
#     examples=[{
#         'name':'Foo',
#         'description':'A very nice Item',
#         'price':35.4,
#         'tax':3.2
#     }],
# ),],
# i2:Annotated[int,Query(description="测试参数",examples=[777])]):
#     results={'item_id':item_id,'item':item}
#     return results




from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results