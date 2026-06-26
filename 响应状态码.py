'''
下面我们将介绍常如何设置响应状态码以及常见的响应状态码
'''

from fastapi import FastAPI,status

app=FastAPI()

@app.post('/items/',status_code=210)
async def create_item(name:str):
    return {'name':name}