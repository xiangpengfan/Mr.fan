'''
fastapi中的查询参数的校验
'''
import random
from fastapi import FastAPI,Query
from typing import Annotated
from pydantic import AfterValidator

app=FastAPI()

data={'name1':'孙悟空','name2':'二郎神','name3':'白骨精'}

def check_name(name):
    for k,v in data.items():    #遍历字典要使用方法.items()
        if name==v:
            return k


# @app.get('/items/')
# async def read_items(q:Annotated[str|None,Query(description='这是一个查询参数',min_length=1,max_length=6,deprecated=True)]=None):
#     results={'name1':'孙悟空','name2':'二郎神','name3':'白骨精'}
#     #键不能重复，重复时，后面的键的值会覆盖前面的
#     if q:
#         results.update({'q':q})
#     return results

@app.get('/items/')
async def read_items(q:Annotated[str|None,AfterValidator(check_name)]):
    if q:
        name=q
        items=data[name]
    else:
        name,items=random.choice(list(data.items()))
    return {'name':name,'items':items}