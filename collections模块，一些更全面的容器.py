'''
一些collections的类的使用
'''

from collections import namedtuple,deque,defaultdict,OrderedDict,ChainMap
import os,argparse

def default_factory():
    return '不存在'

p=namedtuple('p','x y')
q=deque([1,2,3])
d=defaultdict(default_factory)
od=OrderedDict([('a','1'),('b',2),('c',3)])

class LUOrderedDict(OrderedDict):
    def __init__(self,items=None,capacity=10):
        super().__init__()
        self.capacity=capacity
        if items:
            for key, value in items:
                self[key] = value  #这里会调用下面的set方法
    #下面我们要写的是一个解决问题的模板，先判断长度再修改或者添加元素
    #这个写法可以保证我们的代码整体结构清晰，逻辑清晰，后期根据需求修改也非常方便
    def __setitem__(self,key,value):
        containKey=1 if key in self else 0
        if len(self)-containKey>=self.capacity:#这两句代码只做长度判断，不修改元素，保证了代码结构清晰
            last=self.popitem(last=False)
            print('移除：',last)                 #判断我们是否需要移除
        
        if containKey:
            del self[key]
            print('修改',key,value)
        else:
            print('添加',key,value)
        OrderedDict.__setitem__(self,key,value)
        #整体来看，判断长度和判断修改还是添加的代码是分开的，后期维护只需要维护固定模块就可以了

default={'color':'red','user':'guest'} #假设是程序的默认参数
parser=argparse.ArgumentParser() #创建一个参数解析器对象，解析命令行参数
parser.add_argument('-u','--user')#短名用一个短横线长名用两个短横线
parser.add_argument('-c','--color')
namespace=parser.parse_args() #解析命令行参数，返回一个命名空间对象
#命名空间对象类似于字典的映射关系，可以通过点好访问里面的变量
#这里的命名空间对象和解释器里用来传递数据的命名空间有本质不同，不能一概而论
command_line_args={k:v for k,v in vars(namespace).items() if v}
#将namespace里面的参数拿出来，放到一个字典里，并且过滤掉值为None的参数

combind=ChainMap(command_line_args,os.environ,default)
#用ChainMap创建一个新的字典，这个字典包含了很多的小字典
#我们传统的d[key]取值时，会从前往后进行匹配
#它只会返回一个值，找到值后立刻返回不管后面有没有相同的键






if __name__=='__main__':
    # p=p(1,2)
    # print(p.x)
    # q.appendleft('1')
    # print(q)
    # print(q[3])
    # print(d['a'])
    # print(od.keys())
    # lu=LUOrderedDict([(1,2),(2,3),(3,4)],3)
    # lu[4]=5
    print(f'color={combind['color']}')
    print(f'user={combind['user']}') #找到值后立刻返回，不再匹配之后的字典
