'''
类是可调用对象
类可以作为依赖项

类作为依赖项返回的是类创建的实例
'''

from fastapi import FastAPI,Depends
from typing import Annotated


app=FastAPI()

fake_items_db=[{'name1':'foo'},{'name2':'bar'},{'name3':'baz'},
               {'name4':'小熊猫'},{'name5':'小猫'},{'name6':'小狗'},
               {'name7':'小老虎'},{'name8':'小狐狸'},
               {'name9':'小狮子'},{'name10':'小兔子'},
               ]

class Item:
    def __init__(self,q:str|None=None,skip:int=0,limit:int=10):
        self.q=q
        self.skip=skip
        self.limit=limit

Item_depend=Annotated[Item,Depends()]
#这是类依赖项的简便的定义方法，相较于传统的定义方法
#commons: Annotated[依赖类, Depends(依赖类)]
#更加简洁

@app.get('/item/')
async def read_items(item:Item_depend):
    response={}
    if item.q:
        response.update({'q':item.q})
    items=fake_items_db[item.skip:item.skip+item.limit]
    response.update({'items':items})
    return response