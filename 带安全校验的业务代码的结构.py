'''
下面我们将了解，一个业务如果带安全校验，那么它的结构应该是什么样的

必须包含的4个结构块
源pydantic模型
业务部分pydantic模型       #确定数据的完整性和合法性

一个带令牌提取器的依赖项    #保证代码的安全性

负责业务处理的操作主函数
'''

from fastapi import Depends,FastAPI
from pydantic import BaseModel
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

app=FastAPI()

class User(BaseModel):
    username:str
    email:str|None=None
    full_name:str|None=None
    disabled:bool|None=None

def fake_decode_token(token):
    return User(
        username=token+"曹操",
        email="55566@dawei.com",
        full_name="曹孟德",
        disabled=False
    )
#安全性是为了防止数据劫持；模型是为了校验合理数据

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='token')
#这个是捕获器，可以捕获前端发送的令牌

async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    return fake_decode_token(token)
#这是最关键的一步，把安全集成到数据模型上，实现数据安全性保障



@app.get('/users/me')
async def read_users_me(current_user:Annotated[User,Depends(get_current_user)]):
    return current_user

#你会发现User模型贯穿始终