'''
区别于frontend，StaticFiles只能用来挂载资源，基本不会用来挂载前端文件


'''


#我们来模拟挂载几张图片
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app=FastAPI()

app.mount("/",StaticFiles(directory='disk/assets'),name="disk/assets")