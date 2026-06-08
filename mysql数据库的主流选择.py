'''
mysql是数据库的主流选择，一种关系型数据库，安全、免费、稳定
相信我，大多数人选择的数据库准没错
'''

__author__ = '伟大的小熊猫'


import mysql.connector
#依旧是三步走，创建双链接------执行语句------关闭双连接
#我们先创建一个数据库，再创建表单

# with mysql.connector.connect(
#         user='root',
#         password='258456fan',
#         host='127.0.0.1'
#     ) as conn:
#     cursor=conn.cursor()
#     cursor.execute('create database test')
#     conn.commit()




#创建数据库连接
# with mysql.connector.connect(
#         user='root',
#         password='258456fan',
#         database='test',
#         host='127.0.0.1'
#     ) as conn:
#     #创建游标---命令对象
#     cursor=conn.cursor()
#     #执行SQL语句
#     cursor.execute('drop table if exists user')
#     cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#     cursor.execute('insert into user (id,name) values'
#         '(\'1\',\'小熊猫\'),'
#         '(\'2\',\'小狮子\'),'
#         '(\'3\',\'小老虎\'),'
#         '(\'4\',\'小猴子\');'
#     )
#     cursor.rowcount
#     conn.commit()   #提交插入的数据


#查看数据库
with mysql.connector.connect(
    user='root',
    password='258456fan',
    database='test',
    host='127.0.0.1'
    ) as conn:
    cursor=conn.cursor()
    cursor.execute('select * from user')
    value=cursor.fetchall()
    print(value)
