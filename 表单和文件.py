'''
表单和文件可以同时定义
一边接收数据一边接收文件
'''

from typing import Annotated
from fastapi import FastAPI, File, UploadFile,Form

app = FastAPI()

@app.post('/files/')
async def create_file(
    file:Annotated[bytes,File()],
    fileb:Annotated[UploadFile,File()],
    token:Annotated[str,Form()],
    ex:Annotated[UploadFile,File(description='这是一个额外的文件')]
    
):
    content=await ex.read()
    return {
        'file_size':len(file),
        'fileb_content_type':fileb.content_type,
        'token':token,
        'ex_content_type':len(content)
    }
#表单和文件可以同时定义，我们可以同时接收表单数据和文件