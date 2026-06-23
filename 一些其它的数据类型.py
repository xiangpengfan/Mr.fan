#一些其它的数据类型

from datetime import datetime,time,timedelta
from typing import Annotated
from uuid import UUID

from fastapi import FastAPI,Body

app=FastAPI()

@app.put('/items/{item_id}')
async def read_items(
    item_id:int,
    start_datetime:Annotated[datetime,Body()],
    end_datetime:Annotated[datetime,Body()],
    process_before:Annotated[timedelta,Body(description='多长时间之前开始处理的')],
    repeat_at:Annotated[time|None,Body()]=None,
    uuid:Annotated[UUID|None,Body()]=None
):
    start_process=start_datetime+process_before
    if start_process > end_datetime:
        raise HTTPException(status_code=400,detail='开始时间不能晚于结束时间')
    durtion=end_datetime-start_process
    return{
        "item_id":item_id,
        "start_datetime":start_datetime,
        "end_datetime":end_datetime,
        "process_bofore":process_before,
        "repeat_at":repeat_at,
        "start_process":start_process,
        "durtion":durtion
    }