'''
可以添加文档的全局注释
可以已修改文档的缓存地址和文档渲染后的地址

'''

from fastapi import FastAPI

description="""
这里写了一段注释，你可以读到他，另外包含两个api

##项目
你可以读这个项目

##用户
可以创建用户
可以读取用户
"""


tags_metadata=[
    {
        "name":"项目",
        "description":"这是一个项目"
    },
    {
        "name":"用户",
        "description":"这是一个用户",
        "externalDocs":{
            "url":"https://www.baidu.com",
            "description":"这是一个外部文档",
            },
    },
]


app = FastAPI(
    title="一个app",
    description=description,
    summary="这是一个简单的api",
    version="1000",
    terms_of_service="https://www.baidu.com",
    contact={
        "name":"zhangsan",
        "url":"https://www.baidu.com",
        "email":"zhangsan123@qq.com"
    },
    license_info={
        "name":"Apache 2.0",
        "url":"https://www.apache.org/licenses/LICENSE-2.0"
    },

    openapi_tags=tags_metadata,
    docs_url="/666",
    redoc_url=None,
    # openapi_url="/66"
)


@app.get("/users",tags=["项目"])
async def read_users():
    return [{"username":"zhangsan"}]

@app.get("/users/ww",tags=["用户"])
async def read_users():
    return [{"username":"zhangsan"}]


#修改文档地址