'''
有些依赖项重在执行过程，而不需要返回结果

其实准确的说是返回结果的操作被其它操作替代了
校验错误：return---->抛出错误
数据库管理：return---->yield

'''

from typing import Annotated
from fastapi import FastAPI,Header,HTTPException,Depends

app=FastAPI()

async def verify_token(X_token:Annotated[str,Header()]):
    if X_token != 'fake-super-secret-token':
        raise HTTPException(status_code=400,detail='X-token 错啦！')
    
async def verify_key(X_key:Annotated[str,Header()]):
    if X_key != 'fake-super-secret-key':
        raise HTTPException(status_code=400,detail='X-key 错啦！')
    return X_key
#创建两个依赖项，用来校验请求信息，一旦校验失败，就抛出异常
#其实严格来说是结果’return‘被’抛出错误‘替代了


@app.get('/items/',dependencies=[Depends(verify_token),Depends(verify_key)])
async def read_items():
    return [{'items':'Foo'},{'item':'Bar'}]