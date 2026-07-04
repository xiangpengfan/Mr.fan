from fastapi import APIRouter, Form, Depends, Request, HTTPException,Path, Body
from typing import Annotated
from ..dependencise.database_connect import get_session
from sqlmodel import Session, select
from ..model import User
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import os

router=APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}, 
)



# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
# templates = Jinja2Templates(directory=TEMPLATE_DIR)

# # ✅ 这个路由负责"显示登录页面"（GET 请求）
# @router.get("/login")
# async def login_page(request: Request):
#     return templates.TemplateResponse(name="login.html", request=request)

# @router.get("/index")
# def index(request: Request):
#     return templates.TemplateResponse(name="index.html", request=request)


#登录逻辑
@router.post("/login")
def login(username:Annotated[str, Form()],
            password:Annotated[str, Form()],
            session: Annotated[Session, Depends(get_session)],
            ):
    statement=select(User).where(User.username==username)
    user=session.exec(statement).one_or_none() 
    if user and user.password==password:
        return RedirectResponse(url="/index", status_code=302)
    return RedirectResponse(url="/login", status_code=302)


#修改密码逻辑
@router.post("/update")
def update(username:Annotated[str, Form()],
            password:Annotated[str, Form()],
            new_password:Annotated[str, Form()],
            session: Annotated[Session, Depends(get_session)],
            ):
    
    statement=select(User).where(User.username==username)
    user=session.exec(statement).one_or_none() 
    if user and user.password==password:
        try:
            user.password=new_password
            session.commit()
            session.refresh(user)
            return RedirectResponse(url="/index", status_code=302)
        except Exception:
            session.rollback()
            return RedirectResponse(url="/users/update", status_code=302)
    return RedirectResponse(url="/users/update", status_code=302)