from fastapi import FastAPI

app=FastAPI()

name_db=[{'name1':'小红'},{'name2':'小王'},{'name3':'小李'},{'name4':'小赵'},{'name5':'小张'}]

@app.get('/items')
async def read_items(skip:int=0,limit:int=10):
    return name_db[skip:skip+limit]         #这是列表切片查询
#切片查询：list[start : end : step]
#start：起始下标（包含），省略默认 0；
#end：结束下标（不包含），省略默认到末尾；
#step：步长，省略默认 1

# #类型转换
# @app.get('/items/{item_id}')       #这里前面的斜杠不能少
# async def read_item(item_id:str,q:str=None,short:bool=True):
# #这里的id是str类型，short是bool类型
# #输入的数字id会自动转换成str类型，输入的非零数字short会自动转换成true，0是false
#     item={'item_id':item_id}
#     if q:
#         item.update({'q':q})
#     if not short:
#         item.update({'描述':'这代表着你加入了布尔值，他是一个可选查询参数'})
#     return item



#必选参数：必须输入的参数
@app.get('/items/{item_id}')
async def read_user_item(item_id:str,needy:str):
    item={'item_id':item_id,'needy':needy}
    return item