'''
在业务代码中创建真正的校验程序
使业务成为一个真正包含安全验证，并且可以运行的程序

'''

from fastapi import Depends, FastAPI, HTTPException, status
from typing import  Annotated
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

#创建模拟数据库曹操
fake_users_db={
    'johndoe':{
        'username':'caocao',
        'full_name':'曹孟德',
        'email':'cmd@dawei.com',
        'hashed_password':'fake_123456',
        'disabled':False
    },
    'alice':{
        'username':'liubei',
        'full_name':'刘玄德',
        'email':'lb@dahan.com',
        'hashed_password':'fake_123456',
        'disabled':True
    }
}

app=FastAPI()

def fake_hash_password(password: str):
    return "fake_" + password

#创建源模型
class User(BaseModel):
    username:str
    full_name:str|None=None
    email:str|None=None
    disabled:bool|None=None

#创建业务模型
class UserInDB(User):
    hashed_password:str



#创建从数据库中取值的函数，
def get_user(db,username:str):
    if username in db:
        user_dict=db[username]
        return UserInDB(**user_dict)

#捕获令牌并添加错误处理
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='token')
#这个实例可以捕获前端发送的令牌，通过表头Authorization来捕获
async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    print(token)
    user=get_user(fake_users_db,token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='错误的令牌，您不是我们的用户',
            headers={'WWW-Authenticate':'Bearer'}
        )
    return user
#这里暂时拿用户名来代替加密令牌，这并不是实际生产的安全措施，只是临时的演示效果



#创建第二重校验程序
async def get_current_active_user(
        current_user:Annotated[User,Depends(get_current_user)]
        ):
        if current_user.disabled:
             raise HTTPException(
                  status_code=status.HTTP_400_BAD_REQUEST,
                  detail='该数据处于禁用状态，无法访问'
             )
        return current_user


#创建校验程序
@app.post('/token')
async def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
     user_dict=fake_users_db.get(form_data.username)
     if not user_dict:
          raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST,
               detail='用户名错误'
          )
     user=UserInDB(**user_dict)
     hashed_password=fake_hash_password(form_data.password)
     if not hashed_password==user.hashed_password:
          raise HTTPException(
               status_code=status.HTTP_400_BAD_REQUEST,
               detail='密码错误'
          )
     return {'access_token':form_data.username,'token_type':'bearer'}



@app.get('/users/me')
async def read_users_me(
        current_user:Annotated[User,Depends(get_current_active_user)]
        ):   
        return current_user
