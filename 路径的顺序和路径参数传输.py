from enum import Enum
from fastapi import FastAPI

class ModelName(str,Enum):
    alexnet='alexnet'
    resnet='resnet'
    lenet='lenet'     #用来过滤和预设函数值

app=FastAPI()

@app.get('/')
async def root():
    return "message:这是官网，要查询信息请输入模块名称\n可以用http://localhost:8000/models查看模块名称"

@app.get('/models')
async def get_models():
    return "包含以下模块：'alexnet','resnet','lenet'"

@app.get('/models/{model_name}')
async def get_model(model_name:ModelName):
    if model_name==ModelName.alexnet:
        return {'模块名称':model_name,'模块信息':'深度学习在图像识别的开山之作，第一次大幅超越传统方法'}
    if model_name==ModelName.resnet:
        return {'模块名称':model_name,'模块信息':'引入\"残差连接\"，可以训练非常深的网络（152层）'}
    if model_name==ModelName.lener:
        return {'模块名称':model_name,'模块信息':'最简单的卷积神经网络，可以识别手写数字'}

@app.get('/files/{file_path:path}')
async def get_file(file_path:str):
    return {'文件路径':file_path}