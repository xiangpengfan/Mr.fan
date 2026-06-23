'''
请求参数cookie和header
'''

from typing import Annotated
from fastapi import FastAPI,Cookie,Header

app=FastAPI()

# @app.get('/items/')
# async def read_items(id:Annotated[str,Cookie()]=None):
#     return {'id':id}

@app.get('/items/')
async def read_items(id2:Annotated[str,Header()]=None):
     #获取请求头中名为 "id2" 的值
    return {'id2':id2}