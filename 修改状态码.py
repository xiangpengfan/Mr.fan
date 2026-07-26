"""
一个操作函数实现多重业务的设计方法
1.引入多个响应类，每一个业务对应一个响应类
2.对一个响应进行多次修改，简便且优雅
"""

from fastapi import FastAPI,Response,status

app=FastAPI()

tasks={"foo":"Listen to the Bae Fighters"}

@app.put("/tasks/{task_id}",status_code=200)
def create_task(task_id: str,response:Response):
    if task_id not in tasks:
        tasks[task_id]="这个是新加入的"
        response.status_code=status.HTTP_201_CREATED
    return tasks[task_id]
    