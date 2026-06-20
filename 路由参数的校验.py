from fastapi import FastAPI,Path,Query
from typing import Annotated

app=FastAPI()

# @app.get('/items/{item_id}')
# async def read_item(
#     item_id:Annotated[int,Path(title='获取项目的id')],
#     q:Annotated[str,Query(alias='查询参数重命名')]=None
# ):
#     results={'item_id':item_id}
#     if q:
#         results.update({'q':q})
#     return results

@app.get('/items/{item}/{h}')
async def read_item(
    h:Annotated[float,Path(ge=1.5,le=100)],
    #ge=1表示大于等于
    #le=100表示小于等于
    #如果我们只想表示大于和小于，不包括等于，那么gt=1.0,lt=100.0
    item:Annotated[float,Path(gt=0.5,lt=99.5)],
    q:Annotated[str|None,Query(title='查询参数重命名')]=None
    #python语法不允许有默认值的参数在无默认值的参数之前
    #为此我们有三种解决办法
    #通常我们使用参数加Annotated加上默认值来解决
    #另一种方法是在参数前加*使参数变成关键字参数
    #最后，也可以改变一下参数的顺序，但这样参数将无法按照想要的方式排列，会有一些别扭
    
):
    results={'item_id':item}
    if q:
        results.update({'q':q})
    if h:
        results.update({'h':h})
    return results
