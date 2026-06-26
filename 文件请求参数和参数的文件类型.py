'''
表单元数据的变种，可以以二进制形式传输文件
通过files元数据来生成

也可以通过file元数据来生成UploadFile类来声明文件类型
'''

from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post('/files/')
async def create_file(file:Annotated[list[bytes],File(...,description='这是一个文件参数')]):
    return {'文件长度':len(file)}

@app.post('/uploadfile/')
async def create_upload_file(file:Annotated[list[UploadFile],File(...,description='这是一个文件参数')]):
    if not file:
        return {'文件名称':None,'文件长度':None}
    content=await file.read()
    return {'文件名称':file.filename,'文件长度':len(content)}


@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
#这个网页如果有相应代表，前面两个页面的接收多参数是成功运行的