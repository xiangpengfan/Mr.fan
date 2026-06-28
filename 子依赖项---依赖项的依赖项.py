'''
子依赖项是依赖项的依赖项

抽象很多依赖项的重复值
可以帮助我们节省很多的代码量
'''

from typing import Annotated
from fastapi import FastAPI,Cookie,Depends

app=FatAPI()

def little_query(q:str|None=None):
    return q

def big_query(q:Annotated[str|None,Depends(little_query)],
              last_query:Annotated[str|None,Cookie()]
              ):
    if not q:
        return None
    return q,last_query

def big_query2(q:Annotated[str|None,Depends(little_query)],
              last_query2:Annotated[str|None,Query()]
              ):
    if not q:
        return None
    return q
#这两个子依赖项只需要用到一个父依赖项

@app.get('/items/')
async def read_items(query:Annotated[big_query,Depends()]):
    return {'query':query}