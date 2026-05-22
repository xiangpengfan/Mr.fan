'''
一个简单的打造环境的方法
主要包括
@contextmanager
和
closing

环境：隔离，上下文管理和恢复状态
'''

__author__ = "伟大的小熊猫"

from contextlib import contextmanager,closing
import time
from urllib.request import urlopen
import gzip
class Query(object):
    def __init__(self,name):
        self.name=name

    def query(self):
        print(f'目标方法正在执行。。。。{self.name}')

@contextmanager
def new_query(name):
    print('这是打包的__enter__')
    time.sleep(1)
    q=Query(name)
    yield q
    time.sleep(1)
    print('这是打包的__exit__')


with new_query('小熊猫') as q:
    q.query()


with closing(urlopen('https://www.python.org')) as page:
    try:
        content = gzip.decompress(page.read()).decode('utf-8')
    except:
        content = page.read().decode('utf-8')

    for line in content.split('\n'):
        print(line)
#closing其实就是一个简化版的@contextmanager，并且它就是通过@contextmanager编写的
#closing只能给对象加上上下文管理，但无法自定义__enter__和__exit__的内容

#urlopen访问一个数据链接，返回一个响应结果，就是是否完成响应