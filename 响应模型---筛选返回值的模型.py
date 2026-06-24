'''
从外到里输入数据需要设计操作函数的参数的类型，参数类型对应的模型叫请求模型
从里到外输出数据需要设计操作函数的返回值的类型，返回值类型对应的模型叫响应模型

响应模型的参数在路由中输入
'''

from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
from typing import Any

app=FastAPI()

# class Item(BaseModel):
#      name:str
#      description:str|None=None
#      price:float
#      tax:float=None
#      tags:list[str]=[]      #这里设置一个响应模型

#      model_config={
#           'json_schema_extra':{
#                'examples':[
#                     {'name':'橘子','description':'橘子是一种水果','price':42.0,'tags':['水果']},
#                     #{'name':'苹果','description':'苹果是一种水果','price':77.2,'tags':['水果']},
#                ]
#      }
#           }

# @app.post('/items/')
# async def create_item(item:Item)->Item:
#     return item

# @app.put('/items/{item_id}',response_model=list[Item])
# async def update_item()->list[Item]:
#     return [
#         {'name':'橘子','price':42.0,'yy':['水果']},
#         {'name':'苹果','price':77.2},
#     ]


# class UserIn(BaseModel):
#      username:str
#      password:str
#      email:EmailStr
#      full_name:str|None=None

#      model_config={
#           'json_schema_extra':{
#                'examples':[
#                     {
#                          'username':'范冰冰',
#                          'password':'123456',
#                          'email':'5566@qq.com',
#                          'full_name':'小熊猫',
#                          'staus':True
#                     }
#                ]
#           }
#      }

# class UserOut(BaseModel):
#      username:str
#      email:EmailStr
#      full_name:str|None='ccank'
#      status:bool=True

# @app.post('/user/',response_model_exclude_unset=True)
# async def create_user(user:UserIn)->UserOut:
#      return user


class Item(BaseModel):
     name:str
     description:str|None=None
     price:float
     tax:float=None
     tags:list[str]=[]      #这里设置一个响应模型

items={                                 #模拟数据库
     'foo':{
          'name':'橘子',
          'price':42.0,          
     },
     'bar':{
          'name':'苹果',
          'description':'苹果很甜',
          'price':77.2,
          'tax':0.2
     },
     'baz':{
          'name':'香蕉',
          'description':'香蕉很甜',
          'price':33.4,
          'tax':0.7,
          'tags':['水果']
     }
}

@app.get('/items/{item_id}',response_model=Item,response_model_include={'name',"price"})
async def get_item(item_id:str)->Any:
     return items[item_id]      #从数据库中提取数据在这里验证