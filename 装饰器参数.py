'''
装饰器参数用来在交互文档中，给路由或者操作函数添加描述信息
'''

from fastapi import FastAPI,status
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None
    tags:set[str]=[]

@app.post('/items/',status_code=status.HTTP_201_CREATED,tags=['items'])
async def create_item(item:Item):
    return item

@app.post('/items2/',
          tags=['创建文件'],
          summary='根据你的输入创建一个文件',
          description='这里包括文件的详细信息，name，description，price，tax，tags'
          )
async def create_item(item:Item)->Item:
    return item

@app.get('/items2/',tags=['得到文件'],response_description='你试试发送请求，看能不能收到带有描述信息的请求')
async def read_item():
    '''
    我这里会写很长的注释，不知道你能不能看到，
    总之，一句话你给我记好了
    范祥鹏将来有一天会成为一名很厉害的ai开发工程师！！
    '''
    return '宝剑锋从磨砺出，梅花香自苦寒来'

@app.get('/user/',tags=['得到用户名'],deprecated=True)
async def read_item():
    
    return {'用户':'小熊猫'}