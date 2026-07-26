"""
cookie是响应内容的一部分，和响应体同级
cookie主要负责保持登录状态和个性化设置
"""

from fastapi import FastAPI,Response
from fastapi.responses import JSONResponse

app=FastAPI()

#第一种设置cookie的方法
@app.get("/cookie/")
def creat_cookie(response:Response):
    response.set_cookie(key="new_cookie",value="zhi")
    #cookie中不能有中文
    return {"message":"创建cookie"}

#第二种设置cookie的方法
@app.get("/cookie2/")
def creat_cookie2():
    content={"message":"创建cookie2"}
    response=JSONResponse(content=content)
    response.set_cookie(key="new_cookie",value="zhi")
    return response