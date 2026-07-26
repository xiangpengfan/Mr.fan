"""
设置响应头有两种方法：直接使用方法和响应类中增添参数
"""

from fastapi import FastAPI,Response
from fastapi.responses import JSONResponse

app=FastAPI()

@app.get("/headers/")
def get_headers(response:Response):
    response.headers["X-Cat-Dog"]="alone in the world"
    return {"message":"Hello World"}

@app.get("/headers2/")
def get_headers():
    content={"message":"Hello World"}
    headers={"X-Cat-Dog":"alone in the world"}
    return JSONResponse(content=content,headers=headers)