from .dependencise import database_connect
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .routers import users
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
STATIC_DIR = os.path.join(BASE_DIR, "static")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database_connect.create_db_and_tables()
    yield



app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/index")
async def index_page(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(name="login.html",request=request)

@app.get("/users/update")
async def update_page(request: Request):
    return templates.TemplateResponse(name="update.html", request=request)