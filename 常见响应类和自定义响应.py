"""
下面介绍7个常见的响应类和如何自定义响应类

"""

#手写HTMLResponse
from fastapi import FastAPI
from fastapi.responses import HTMLResponse,Response,PlainTextResponse,FileResponse,StreamingResponse,RedirectResponse
from fastapi.responses import orjson
import asyncio

# app=FastAPI()

# # @app.get("/items/",response_class=HTMLResponse)
# # async def read_items():
# #     return """
# #     <html>
# #         <head>
# #             <title>这是一个HTML</title>
# #         </head>
# #         <body>
# #             <h1>这是第一行内容</h1>
# #         </body>
# #     </html>
# #     """

# # @app.get("/items/")
# # async def read_items():
# #     data="""
# #     <html>
# #         <head>
# #             <title>这是一个HTML</title>
# #         </head>
# #         <body>
# #             <h1>这是第一yi行内容</h1>
# #         </body>
# #     </html>
# #     """
# #     return HTMLResponse(content=data)


# #Response是所有响应的父类，可以自定义任何响应
# @app.get("/legacy/")
# def get_legacy_data():
#     data="""
#     <html>
#         <head>
#             <title>这是一个HTML</title>
#         </head>
#         <body>
#             <h1>这是第内容</h1>
#         </body>
#     </html>
#     """
#     return Response(content=data,media_type="text/html")


# #HTMLResponse上文介绍的那样
# #PlainTextResponse返回纯文本，接收纯文本和字节
# @app.get("/items/",response_class=PlainTextResponse)
# async def read_items():
#     return "Hello World"


# #JSONResponse参考上文
# #FileResponse发送文件，打开链接直接下载文件
# @app.get("/typer")
# async def typer():
#     return FileResponse("test_file")


# #StreamingResponse流式传输的底层类
# async def streamer():
#     for i in range(5):
#         yield b"Hello World"
#         await asyncio.sleep(1)

# @app.get("/stream")
# async def stream():
#     return StreamingResponse(streamer())


# #RedirectResponse返回重定向，接收url
# @app.get("/redirect")
# async def redirect():
#     return RedirectResponse("https://www.baidu.com",status_code=300)

# class CustomJSONResponse(Response):
#     media_type = "application/json"

#     def render(self, content):
#         assert orjson is not None, "orjson is not installed."
#         return orjson.dumps(content)

# @app.get("/custom_hson")
# async def custom_hson():
#     return CustomJSONResponse({"hello": "world"})

app=FastAPI(default_response_class=HTMLResponse)

@app.get("/")
async def root():
    return "<h1>任务结束</h1><p>小熊猫，你真的很棒</p>"