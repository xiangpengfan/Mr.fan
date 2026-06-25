'''
下面我将介绍其它类型的响应模型
包括多类型响应模型、泛型、字典。。。。
从一组贴近实际应用的多模型入手
'''

#这是一个用户信息保存到数据库并经过筛选输出的程序
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app=FastAPI()

class Base(BaseModel):
     username:str
     email:EmailStr
     description:str|None=None

class UserIn(Base):
     password:str
     model_config={
          'json_schema_extra':{
               'examples':[
                    {
                         'username':'小熊猫',
                         'description':'小熊猫一定会得到胜利',
                         'email':'xxxmmmm@qq.com',
                         'password':'554466'
                    }
               ]
          }
     }


class UserOut(Base):
     pass
class UserInDB(Base):
     hashed_password:str
     
def fake_password_hash(raw_password:str):   #raw原始的
     return "salt"+raw_password

def fake_save_password(user_in:UserIn):
     hash_password=fake_password_hash(user_in.password)
     user_in_db=UserInDB(**user_in.dict(),hashed_password=hash_password)
     print(f'密码处理后的数据在这里保存到数据库，处理后的密码{hash_password}')
     return user_in_db

@app.post('/user/',response_model=UserOut)
async def create_user(user:UserIn):
     user_saved=fake_save_password(user)
     return user_saved     #这里保存到数据库并且经过筛选后把他们输出给客户端
