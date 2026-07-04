from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str=Field(index=True, unique=True)
    password: str
    phone:str=Field(index=True)

# class Login_model(SQLModel):
#     username: str
#     password: str