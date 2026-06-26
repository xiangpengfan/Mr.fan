'''
一种新的元数据，表单数据
通过Form来生成

同样，表单类型的数据类型也可以声明pydantic模型
'''

from typing import Annotated
from fastapi import FastAPI,Form,Body
from pydantic import BaseModel

app=FastAPI()

class FormData(BaseModel):
    username:str
    password:str


@app.post('/login/')
async def login(username:Annotated[str,Form()],password:Annotated[str,Form()],user_agent:Annotated[str,Body()]):
    return {'username':username,'password':password,'user_agent':user_agent}

@app.post('/login2/')
async def login2(form_data:Annotated[FormData,Form()]):
    return form_data
#表单参数即使声明pydantic模型，依然是一条一条是输入数据
