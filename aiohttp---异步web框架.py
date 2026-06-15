'''
aiohttp是一种异步web框架，更复杂但是性能更好，适用于大量的并发请求
'''

__author__='伟大的小熊猫'

from aiohttp import web

async def index(request):              #创建一个网站首页
    text='<h1>欢迎来到小熊猫的官网</h1>'      
    return web.Response(text=text,content_type='text/html')

async def hello(request):
    name=request.match_info.get('name','小熊猫')   #获取URL中的参数，获取信息的一种
    text=f'<h1>你好啊,{name}</h1>'
    return web.Response(text=text,content_type='text/html')

app=web.Application()

app.add_routes([web.get('/',index),web.get('/{name}',hello)])


if __name__=='__main__':
    web.run_app(app)         #默认端口是8080