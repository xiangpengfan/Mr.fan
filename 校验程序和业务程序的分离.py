'''
fastapi安全性入门：解耦校验程序和业务程序
'''

from typing import Annotated
from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")

@app.get('/items/')
async def read_times(token:Annotated[str,Depends(oauth2_scheme)]):
    return {'token':token}