'''
中间件是一个函数
中间件位于请求和操作之间
中间件可以对请求和响应做额外一步的处理

'''

import time
from fastapi import FastAPI, Request

app=FastAPI()

@app.get("/")
async def call_next(s:str):
    return {"message": "Hello World"}

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time=time.time()
    reponse=await call_next(request)
    process_time=time.time()-start_time
    reponse.headers['X-Process-Time']=str(process_time)
    return reponse

@app.middleware("http")
async def log_request(request: Request, add_process_time_header):
    reponse=await add_process_time_header(request)
    reponse.headers['X-Process-Time2']=str('yangcong_waiceng')
    return reponse