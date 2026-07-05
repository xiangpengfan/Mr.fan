'''
sse是一种流式传输的特殊的json响应格式的数据

'''
import time
import asyncio
from collections.abc import AsyncIterator
#这个是异步解析器

from fastapi import FastAPI,Header
from fastapi.sse import EventSourceResponse,ServerSentEvent
from pydantic import BaseModel
from typing import Annotated





app=FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None

items = {
    "foo": {"name": "Foo1", "description": "There are many like it, but this one is mine."},
    "bar": {"name": "Bar2", "description": "There are many like it, but this one is mine."},
    "baz": {"name": "Baz3", "description": "There are many like it, but this one is mine."},
    "foo1": {"name": "Foo4", "description": "There are many like it, but this one is mine."},
    "bar1": {"name": "Bar5", "description": "There are many like it, but this one is mine."},
    "baz1": {"name": "Baz6", "description": "There are many like it, but this one is mine."},
    "111foo": {"name": "Foo7", "description": "There are many like it, but this one is mine."},
    "111bar": {"name": "Bar8", "description": "There are many like it, but this one is mine."},
    "111baz": {"name": "Baz9", "description": "There are many like it, but this one is mine."},
    "11foo": {"name": "Foo10", "description": "There are many like it, but this one is mine."},
    "11bar": {"name": "Bar11", "description": "There are many like it, but this one is mine."},
    "11baz": {"name": "Baz12", "description": "There are many like it, but this one is mine."},
    "1foo": {"name": "Foo13", "description": "There are many like it, but this one is mine."},
    "1bar": {"name": "Bar14", "description": "There are many like it, but this one is mine."},
    "1baz": {"name": "Baz15", "description": "There are many like it, but this one is mine."},
    "xfoo": {"name": "Foo16", "description": "There are many like it, but this one is mine."},
    "xbar": {"name": "Bar17", "description": "There are many like it, but this one is mine."},
    "xbaz": {"name": "Baz18", "description": "There are many like it, but this one is mine."},
    "xfoo1": {"name": "Foo19", "description": "There are many like it, but this one is mine."},
    "xbar1": {"name": "Bar20", "description": "There are many like it, but this one is mine."},
    "xbaz1": {"name": "Baz21", "description": "There are many like it, but this one is mine."},
    "x111foo": {"name": "Foo22", "description": "There are many like it, but this one is mine."},
    "x111bar": {"name": "Bar23", "description": "There are many like it, but this one is mine."},
    "x111baz": {"name": "Baz24", "description": "There are many like it, but this one is mine."},
    "x11foo": {"name": "Foo25", "description": "There are many like it, but this one is mine."},
    "x11bar": {"name": "Bar26", "description": "There are many like it, but this one is mine."},
    "x11baz": {"name": "Baz27", "description": "There are many like it, but this one is mine."},
    "x1foo": {"name": "Foo28", "description": "There are many like it, but this one is mine."},
    "x1bar": {"name": "Bar29", "description": "There are many like it, but this one is mine."},
    "x1baz": {"name": "Baz30", "description": "There are many like it, but this one is mine."},
}
# @app.get("/items/stream",response_class=EventSourceResponse)   #作用是将数据解码成sse的json格式
# async def read_item():
#     for item in items.values():
#         time.sleep(0.05)
#         yield item

@app.get("/items",response_class=EventSourceResponse)
async def read_items():
    for item in items.values():
        time.sleep(0.5)
        yield ServerSentEvent(type="message",data=item)

@app.get("/items/stream",response_class=EventSourceResponse)
async def read_item(last_event_id:Annotated[str|None,Header()]=None):
    start = last_event_id+1 if last_event_id else 0
    for i,item in enumerate(items.values()):
        if i<start:
            continue
        await asyncio.sleep(3)
        yield ServerSentEvent(type="message",data=item,retry=1000)
