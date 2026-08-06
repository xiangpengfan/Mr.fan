"""
不再使用类作为依赖项而是使用类的实例作为依赖项

一类多用了说是
"""


from typing import Annotated
from fastapi import FastAPI,Depends

app=FastAPI()

class FixedContentChecker:
    def __init__(self,fixed_content:str):
        self.fixed_content=fixed_content

    def __call__(self,q:str=""):
        if q:
            return self.fixed_content in q
        return False

checker=FixedContentChecker("bar")

@app.get("/query/")
async def read_query_check(fixed_content_included:Annotated[bool,Depends(checker)]):
    return {"fault":fixed_content_included}
    