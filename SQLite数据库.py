'''
sqlite数据库是一款python已经加载了它的驱动的数据库
它的数据储存就是一个文件
数据库本身占用内存极小，启动迅速，常常被嵌入app或者小型web应用中
被称为嵌入式数据库
'''

__author__ = '伟大的小熊猫'


import os,sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
conn.commit()
cursor.close()
conn.close()

def get_score_in(low,high):
    with sqlite3.connect(db_file) as conn:
        cursor=conn.cursor()
        cursor.execute('select name,score from user where score between ? and ? order by score',(low,high))
        #order by score是从小到大排序，从大到小为order by score desc
        values=cursor.fetchall()
        name_data=[]
        for v in values:          
            name_data.append(v[0])
    return name_data

if __name__ == '__main__':
    assert get_score_in(80, 95) == ['Adam']
    assert get_score_in(60, 80) == ['Bart', 'Lisa']
    assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam']
    print('测试通过!')