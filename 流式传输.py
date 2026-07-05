'''
将字符串或者一个大文件切分成小块进行传输，
每次一小块一小块的传输，
这种传输方式叫做流式传输
'''

from fastapi import FastAPI
from pydantic import BaseModel
from collections.abc import AsyncIterable,Iterable

app=FastAPI()

class Item(BaseModel):
    name:str
    description:str|None

items=[
    Item(name="Foo",description="这是第一个数据"),
    Item(name="Bar",description="这是第二个数据"),
    Item(name="Baz",description="这是第三个数据"),
]

@app.get('/items')
async def read_items()->AsyncIterable[Item]:
    for item in items:
        yield item