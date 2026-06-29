'''
带有yield的依赖项常用在需要上下文管理的场景，如：数据库、外部 API、文件系统等

yield依赖项可以实现连接的自动销毁，文件的自动关闭，相当于python中的with语句
不同之处在于，他是跨操作函数的自动关闭，with语句只能在一个函数内使用
'''

from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated


app=FastAPI()

data={
    'plumbus':{'description':'名词堆砌的无用概念','owner':'莫蒂'},
    'portal-gun':{'description':'创造传送门的枪','owner':'瑞克'},
}

class OwerError(Exception):
    pass

def get_username(p_value:str):
    try:
        yield p_value
    except OwerError as e: 
        raise HTTPException(status_code=444,detail='在数据库中有这个值，但是这不是我们要找的值')
#函数是依赖项，加装饰器的函数可以是错误处理器


@app.get('/items/{item_id}')
async def read_item(item_id:str,username:Annotated[str,Depends(get_username)]):
    
    if item_id not in data:
        raise HTTPException(status_code=400,detail='根本没有这个值')
    item=data[item_id]
    if item['owner']!=username:
        raise OwerError()
    return item