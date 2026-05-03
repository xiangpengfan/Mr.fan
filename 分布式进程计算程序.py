'''
分布式进程计算程序
'''

__author__='伟大的范先生'

import time,random,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('task_queue')
QueueManager.register('result_queue')                            #取之前先把名字记下来，就像买东西先列清单一样
if __name__=='__main__':
    manager=QueueManager(address=('192.168.100.103',5000),authkey=b'abc')
    manager.connect()              #连接到服务器，也就是Master

    task=manager.task_queue()              #注意，队列创建时就是一个函数，所以这里要调用这个函数才能得到队列对象
    result=manager.result_queue()          #但是这里可以理解为把一个值赋值给一个变量

    for i in range(10):
        n=task.get(timeout=1)      #从任务队列获取任务，get方法会一直等待直到拿到任务，timeout参数设置1秒钟，如果1钟还没有拿到任务就报错
        print(f'正在对整数{n}进行3阶乘处理...')
        r=n*n*n
        time.sleep(1)
        result.put(r)              #把结果放入结果队列，put方法会把结果放入队列中，等待Master来取
