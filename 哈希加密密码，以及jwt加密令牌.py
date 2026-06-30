'''
把安全性校验分成两部分，一部分验证哈希密码的准确性，另一部分在发送令牌时加上jwt的包装

'''
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import FastAPI, HTTPException, Depends, Query, Path, status
from pydantic import BaseModel
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pwdlib import PasswordHash
from jwt.exceptions import InvalidTokenError

import tracemalloc

tracemalloc.start()

SCREET_KEY='x7K9mN2pR5fQwE8vB4zL6yX1cJ3hU7sA0dF'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30


fake_users_db={
    "caocao": {
        "username": "caocao",
        "full_name": "曹孟德",
        "email": "5566001@dawei.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$KfbStwiXZZXdjmnTp0oV2A$8aRCKYyD7SYbGXSH1QhBSAjspJxJGORC+LG2yCFX5Q4",
        "disabled": False,
    },
    'liubei':{
        "username": "liubei",
        "full_name": "刘备",
        "email": "5566002@dahan.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$+y1pPGm/5viTY13hvMENPA$CkZF3Xt/dxxPuBi8ZthQ3txNnLHGSXrr401/JGAGyfo",
        "disabled": False
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str

# password_hash=PasswordHash.recommended()
# password='654321'
# hpassword=password_hash.hash(password)
# print(hpassword)

app=FastAPI()

#安全校验分为两步，账号+哈希密码验证；jwt加密令牌

password_hash=PasswordHash.recommended()

#账号密码验证所需要的小函数
def verify_password(plain_password,hashed_password):
    return password_hash.verify(plain_password,hashed_password)


#账号+哈希密码验证
async def authenticate_user(fake_db,username:str,password:str):
    user=fake_db.get(username)
    if not user:
        verify_password(password,'12345')   
        #这里的verify_password是同步程序各个细分路径的运行时间，以免遭受时间攻击
        #时间攻击会根据时间差计算出账号是否存在
        return False
    if not verify_password(password,user['hashed_password']):
        return False
    return user

#jwt加密令牌:jwt加密需要，
# 动态参数：内容+过期时间，全部输入字典中；
# 静态参数：加密密钥+算法，在jwt加密时输入
async def create_access_token(data:dict,expires_delta:timedelta|None=None):
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.now(timezone.utc)+expires_delta
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=15)
    to_encode.update({'exp':expire})
    encoded_jwt=jwt.encode(to_encode,SCREET_KEY,ALGORITHM)
    return encoded_jwt

@app.post('/token')
async def login(form_data:OAuth2PasswordRequestForm=Depends(),
        )->Token:
    user=await authenticate_user(fake_users_db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token=await create_access_token({'sub':user['username']},timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return Token(access_token=access_token,token_type='bearer')




class User(BaseModel):
    username:str=None
    full_name:str=None
    email:str=None
    disabled:bool=None

class UserInDB(User):
    hashed_password:str


#我们把数据库提取数据给摘出来，因为他很重要
def get_user(fake_users_db,username:str):
    if username in fake_users_db:
        user_dict=fake_users_db[username]
        return UserInDB(**user_dict)

#创建接收代码
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="不是无效的令牌",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload=jwt.decode(token,SCREET_KEY,algorithms=[ALGORITHM])
        username=payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data=TokenData(username=username)
        #这一步过滤是干什么的
    except InvalidTokenError:
        raise credentials_exception
    user=get_user(fake_users_db,username=token_data.username)
    if user is None:
        raise credentials_exception
    return user



#返回值验证
async def get_current_activated_user(current_user:Annotated[UserInDB,Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400,detail='用户被禁用')
    return current_user




    


@app.get('/users/me')
async def read_users_me(current_user:Annotated[dict,Depends(get_current_activated_user)]):
    return current_user

@app.get('/users/me/items')
async def read_own_items(current_user:Annotated[UserInDB,Depends(get_current_activated_user)]):
    return [{'item_id': 'Foo', 'owner': current_user.username}]

@app.put('/users/{modify_password}')
async def modify_password(modify_password:Annotated[str,Path(description='新值')],
        username:Annotated[str,Query(description='当前用户名')]):
    if username not in fake_users_db:
        raise HTTPException(status_code=404,detail='用户不存在')
    fake_users_db[username]['hashed_password']=password_hash.hash(modify_password)
    return {'message':'密码修改成功'}