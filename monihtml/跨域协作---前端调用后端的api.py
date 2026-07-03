'''
前端在调用后端的api时需要进行跨域协作

这里设置一个后端api等待前端调用
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

allowed_origins=[
    'http://localhost:3000'

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  #允许的源的白名单
    allow_credentials=True,         #允许cookie传入
    allow_methods=["*"],            #允许访问所有的请求方法
    allow_headers=["*"],            #允许所有的请求头通过
)

@app.get('/')
async def root():
    return "message:访问成功，跨域成功！！"