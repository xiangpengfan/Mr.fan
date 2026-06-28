'''
全局依赖项，任何一个函数都会触发的依赖项
默认做拦截作用，返回值不会输出

其实就相当于给每一个函数创建了一个无返回值的依赖项

'''

from typing import Annotated
from fastapi import FastAPI,Depends,HTTPException,Header

async def verify_token(x_token:Annotated[str,Header()]):
    if x_token != "fake-token":
        raise HTTPException(status_code=401,detail="X-Token 错啦！！")
    
async def verify_key(x_key:Annotated[str,Header()]):
    if x_key != "fake-key":
        raise HTTPException(status_code=401,detail="X-Key 错啦！！")
    
app=FastAPI(dependencies=[Depends(verify_token),Depends(verify_key)])

@app.get('/items/')
async def read_items():
    return [{"item":"小王"},{"item":"李世民"}]

@app.get('/users/')
async def read_users():
    return [{"user":"尉迟敬德"},{"user":"秦叔宝"}]