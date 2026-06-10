'''
SQLAichemy是一个优秀的ORM框架，具体来说它的优点有两个：
1.它允许我们用操作类的方法来操作数据库
2.它自定义了多线程线程池、事务自动处理、连接复用等功能
'''

__author__ = '伟大的小熊猫'


from sqlalchemy import Column,String,create_engine,ForeignKey    #这是连接，类似于conn
from sqlalchemy.orm import sessionmaker,relationship  #这是会话，类似于cursor,但不同的是使用的时候我们需要先创建实例
from sqlalchemy.orm import declarative_base #这是基类,把数据库表单变成类的关键一步

Base=declarative_base()

class User(Base):       #一个类关联数据库中的一个表
    __tablename__='user'#这是数据库中对应的表名
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    book=relationship('Book')
    def __repr__(self):   #当我们打印对象时，这个方法可以显示打印出的结果
        return f'作家：{self.name}'  #这时候的self代表的是调用的全部内容
class Book(Base):
    __tablename__='book'
    id=Column(String(20),primary_key=True)
    book_name=Column(String(128)) 
    #如果这里的列名或者叫字段名定义错了，只能去数据库里面修改，或者用Alembic，正规项目里会采用
    user_id=Column(String(20),ForeignKey('user.id'))

    def __repr__(self):
        return f'作品：{self.book_name}'

engine=create_engine('mysql+mysqlconnector://root:258456fan@localhost:3306/test')
#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
#Base.metadata.create_all(engine)
DBSession=sessionmaker(bind=engine)
# session=DBSession() #创建会话，真正的操作数据库的对象
# session.add(Book(id='1',detail='小熊猫的修炼手册',user_id='1'))
# session.add(Book(id='2',detail='小狮子的心情日记',user_id='2'))
# session.commit()
# session.close()

session=DBSession()
user=session.query(User).filter(User.id=='1').one()
print(user)
print(user.book)
session.close()