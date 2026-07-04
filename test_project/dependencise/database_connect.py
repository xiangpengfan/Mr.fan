from sqlmodel import SQLModel,Session,create_engine

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:258456fan@localhost:3306/login?charset=utf8mb4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    #  connect_args={"server_public_key": "./public_key.pem"}
    )

Base = SQLModel   #Base这个名称是行业固定标准

#创建数据库表单
async def create_db_and_tables():
    Base.metadata.create_all(engine)

#创建会话
def get_session():
    with Session(engine) as session:
        yield session

