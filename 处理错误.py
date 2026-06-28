'''
可以自定义声明异常，也可以创建新的错误类型
'''

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.encoders import jsonable_encoder 
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler
)

# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name
#自定义异常类名称和属性 



app=FastAPI()

# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request, exc):
#     return JSONResponse(
#         status_code=411,
#         content=jsonable_encoder({"detail":exc.errors(),"body":exc.body})
#     )
#当UnicornException错误被触发时，会调用这个处理函数
#这两个参数是固定的，是用来方便做错误处理的
# 前面代表了请求对象，是我们接收到的请求数据；
# 后面是错误对象，是我们定义的那个错误类


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc: RequestValidationError):
#     message='这是一个已经被定义的错误类型，我们修改它的处理方法'
#     for error in exc.errors():   #从错误对象中提取错误信息，把错误信息拼接到message中
#         message+=f'\nField:{error["loc"]},Error:{error["msg"]}\n'
#     return PlainTextResponse(content=message,status_code=400)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    print(f'警告！警告！发现了一个错误{exc}。。。。')
    return await request_validation_exception_handler(request,exc)


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request,exc):
#     print('这个错误被执行了')
#     return PlainTextResponse(str(exc.detail),status_code=exc.status_code)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request,exc):
    print(f'你输错了一个值，再检查检查：{exc}')
    return await http_exception_handler(request,exc)

# class one(BaseModel):
#     name:str
#     age:int
#     score:float

# items={
#     "foo": "这是第一个数据",
#     "bar": "这是第二个数据"
# }

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=444,
#                             detail="没有找到这个数据",
#                             headers={"X-Header": "The response headers"}
#                             )
#     return {"item": items[item_id]}

# @app.post('/unicorns/{name}')
# async def read_unicorn(name:str):
#     if name=='yolo':
#         raise UnicornException(name=name)
#     return {'unicorn_name':name}

@app.get('/items2/{item_id}')
async def read_item(item_id:int):
    
    if item_id<0:
        raise HTTPException(status_code=400,detail='请输入大于0的数字')
    return {'item_id':item_id}

# @app.exception_handler(RequestValidationError)
# async def http_exception_handler(request,exc):
#     return JSONResponse(
#         status_code=422,
#         content=jsonable_encoder({"detail":exc.errors(),'body':exc.body}),
#         )

# class Item(BaseModel):
#     title:str
#     size:int

# @app.post('/items/')
# async def create_item(item:Item):
#     return item