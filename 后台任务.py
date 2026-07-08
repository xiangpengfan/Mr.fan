'''
后台任务是在响应结束后继续运行的任务
实现方法/类：BackgroundTasks

'''
from fastapi import FastAPI, BackgroundTasks,Depends
from typing import Annotated

app=FastAPI()

# def write_notification(email: str,message=""):
#     with open("log.txt",mode="a",encoding="utf-8") as email_file:
#         content=f"收到通知 {email}:{message}\n"
#         email_file.write(content)

# @app.post("/send-notification/{email}")
# async def send_notification(email:str,background_task:BackgroundTasks):
#     background_task.add_task(write_notification,email,message='这是一条日志信息，以后或许会是报错信息')
#     return {"message": "信息发送成功"}



#嵌套的后台任务：一个后台任务嵌套另一个后台任务，api会按按照洋葱模型执行
#洋葱模型：先执行最外层的后台任务，再执行最内层的后台任务

#这是内层的后台任务：后执行
def write_log(message:str):
    with open("log2.txt",mode="a",encoding="utf-8") as log_file:
        message=f"{message}\n"
        # print(message)
        log_file.write(message)

#这是外层的后台任务：先执行
def get_query(background_tasks:BackgroundTasks,q:str|None=None):
    if q:
        message=f"查询参数是{q}"
        # print(message)
        background_tasks.add_task(write_log,message)
        return {"message":"第二次信息发送成功"}
    return {"message":"查询参数未添加"}
    
@app.post("/send-notification/{email}")
async def send_notification(
    email:str,
    background_tasks: BackgroundTasks,
    q: Annotated[str,Depends(get_query)]   #这里是第一次写入日志，函数调用写入函数
):
    # print(q)
    message=f"收到通知 {email}"
    background_tasks.add_task(write_log,message)    #这里是直接调用写入函数
    return {"message": "信息发送成功"}
#这种嵌套可以使很多业务函数直接调用后台任务函数写入日志，而不需要重新写写入逻辑