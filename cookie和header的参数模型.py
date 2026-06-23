from typing import Annotated
from fastapi import FastAPI, Header, Cookie
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
     session_id:str
     fatebook_tracker:str|None=None
     googall_tracker:str|None=None

class header(BaseModel):
     host:str
     save_data:bool
     if_modified_since:str|None=None
     traceparent:str|None=None
     x_tag:list[str]|None=None

@app.get('/items/')
async def read_items(cookies:Annotated[Item, Cookie()]):
     return cookies
#将会看到错误信息因为浏览器不允许我们轻易访问cookie

@app.get('/headers/')
async def read_headers(headers:Annotated[header,Header()]):
     return headers
