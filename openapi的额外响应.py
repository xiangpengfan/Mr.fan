"""
一个操作函数可以声明多个响应，if return else return
但是路由response_class只能添加一个响应在交互文档中
附加响应用来在交互文档中添加除了主响应外的额外的响应注释
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse,FileResponse
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id:str
    value:str

class Message(BaseModel):
    message:str


responses={
    404:{"description":"没有找到"},
    302:{"description":"这个网页被转移了"},
    403:{"description":"没有权限"}
}

@app.get("/itemss/{item_id}",response_model=Item,responses={404:{"model":Message}})
async def read_item(item_id:str):
    if item_id=="foo":
        return {"id":"foo","value":"这是我的英雄"}
    return JSONResponse(content={"message":"没有这个英雄"},status_code=404)

@app.get("/item/{item_id}",response_model=Item,
        # responses={
        #     200:{
        #         "content":{"image/png"},
        #         "description":"返回图片"
        #     },
        #     404:{"model":Item,"description":"没有这个英雄"}
        # }
        responses={
            **responses,
            200:{"content":{"image/png"},"description":"返回图片"}
        }
         )
async def read_item(item_id:str,img:bool|None=None):
    
    if img:
        return FileResponse("img.png",media_type="image/png")
    else:
        return JSONResponse(content={"message":"没有111这个英雄"},status_code=404)


