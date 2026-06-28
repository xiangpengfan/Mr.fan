'''
依赖项是fastapi的核心，学完之后做一个小练习
'''

from typing import Annotated
from fastapi import FastAPI, Depends

app=FastAPI()

async def common_parameters(
        q:str|None=None,
        skip:int=0,
        limit:int=100
):
    return {"q":q,"skip":skip,"limit":limit}

commons=Annotated[dict,Depends(common_parameters)]
#这里的commons就是依赖项，直接声明数据类型

@app.get("/items/")
async def read_items(commons:commons):
    
    return commons

@app.get("/users/")
async def read_users(commons:commons):
    return commons