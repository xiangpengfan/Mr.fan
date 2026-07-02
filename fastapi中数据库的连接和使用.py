'''
以sqllite为例
介绍数据库如何再fastapi中连接和使用

'''

from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status,Query
from sqlmodel import Session,Field,SQLModel,create_engine,select
from contextlib import asynccontextmanager

#创建模型
class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int
    life_story: str

class Hero(HeroBase, table=True):
    id: Annotated[int|None, Field(primary_key=True, default=None)]
    #这里的None表示接收的数据id的值可以为空，数据库自动分配
    secret_identity: str | None = None

    
class HeroPublic(HeroBase):
    id: int

class HeroCreate(HeroBase):
    secret_identity: str

class HeroUpdate(SQLModel):
    name: str | None = None
    age: int | None = None
    secret_identity: str | None = None
    life_story: str | None = None


#创建数据库
engine = create_engine("sqlite:///fastapi_test_db.db",connect_args={'check_same_thread':False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    print("数据库创建成功")
    yield
    print("数据库关闭....")

app=FastAPI(lifespan=lifespan)
#可以添加错误处理

def print_data(hero):
    print(f'姓名:{hero.name}')
    print(f'年龄:{hero.age}')
    print(f'经历:{hero.life_story}')
    print(f'身份:{hero.secret_identity}')
    print(f'ID：{hero.id}')


#创建增删改查操作--删查增改
#创建删除操作
@app.delete("/heroes/{hero_id}", status_code=status.HTTP_204_NO_CONTENT,response_description="响应成功",tags=["删除数据"])
async def delete_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="这个英雄不存在，无法删除")
    session.delete(hero)
    session.commit()
    print(f"英雄{hero.name}已经被删除")

#创建查找操作
#创建查找多个数据
@app.get("/heroes", response_model=list[HeroPublic],tags=["查找多个数据"])
async def read_heroes(session: Annotated[Session,Depends(get_session)],skip: int = 0, limit: int = 100):
    heroes = session.exec(select(Hero).offset(skip).limit(limit)).all()
    for hero in heroes:
        print_data(hero)
        print('------------------')
    return heroes
#创建查找单个数据
@app.get("/heroes/{hero_id}", response_model=HeroPublic,tags=["查找单个数据"])
async def read_hero(hero_id:int,session: Annotated[Session,Depends(get_session)]):
    hero=session.get(Hero,hero_id)
    if not hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="这个英雄不存在，请检查输入是否有误")
    print_data(hero)
    return hero

#创建增加数据操作
@app.post('/heroes',response_model=HeroPublic,tags=["增加数据"])
async def create_hero(hero:HeroCreate,session: Annotated[Session,Depends(get_session)]):
    db_hero=Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    print('增加数据')
    print_data(db_hero)
    return db_hero

#创建更新操作
@app.put('/heroes/{hero_id}',response_model=HeroPublic,tags=["更新数据"])
async def update_hero(hero_id:int,hero:HeroUpdate,session: Annotated[Session,Depends(get_session)]):
    db_hero=session.get(Hero,hero_id)
    #这里取出来的是Hero类的实例
    if not db_hero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="这个英雄不存在,无法更新")
    hero_data=hero.model_dump(exclude_unset=True)
    #把模型转换成字典，并且只提取用户输入的部分
    db_hero.sqlmodel_update(hero_data)
    session.commit()
    session.refresh(db_hero)
    print('更新数据')
    print_data(db_hero)
    return db_hero
    #这里让用户知道自己更新的是哪个数据
