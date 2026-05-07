'''
一个datetime模块的使用示例
'''

__author__ = "伟大的小熊猫"

from datetime import datetime,timedelta,timezone
import re

def to_timestamp(dt_str,tz_str):
    dt=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')#字符串转化成时间对象
    m=re.match(r'UTC([+-]\d{1,2}):00',tz_str) #把字符串的关键参数提出来
    tz = timezone(timedelta(hours=int(m.group(1)))) #创建一个时区对象
    tz_UTC5=dt.replace(tzinfo=tz)#给时间加上时区对象
    return tz_UTC5.timestamp()

if __name__=='__main__':    
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2

    print('测试成功')
# if __name__=='__main__':
#     m=re.match(r'UTC[+-](\d{1,2}):00','UTC+7:00')
#     #tz=datetime.strptime('UTC+7:00','UTC%z')
#     print(m.group(1))