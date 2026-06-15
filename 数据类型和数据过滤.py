from typing import Any
import random
from pydantic import BaseModel
from datetime import datetime

# def xiaoming(subject:dict[str,float],hoppy:str|None,saying:Any):
#     l1,l2=[],[]
#     for k,v in subject.items():
#         l1.append(k)
#         l2.append(v)
#     index=random.randint(0,len(l1)-1)
#     print(f'小明的{l1[index]}得了{l2[index]}分，爱好是{hoppy}，成功名言是:{saying}')

# xiaoming({'语文':90,'数学':80,'英语':70},'学编程','宝剑锋从磨砺出，梅花香自苦寒来。')  


class User(BaseModel):
    id:int
    name:str='John Doe'
    signup_ts:datetime|None=None
    friends:list[str]=[]    
    
Raw_data={
    'id':'123',
    'signup_ts':'2017-06-01 12:22',
    'friends':['1','小红','小王'.encode('utf-8')],  #注意这里的小王是bytes
    #basemodel会在一定程度上把数据转化为对应的数据类型
}

user=User(**Raw_data)
print(user)
print(user.id,user.signup_ts,user.friends)