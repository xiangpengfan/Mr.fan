'''
这组程序模拟了处理一个复杂任务时多进程协作的场景，一种Master/Worker模式。
这个程序是Master
负责发送任务关键数据和接收结果
'''

__author__ ='伟大的范先生'




import time,random,queue
from multiprocessing.managers import BaseManager
from multiprocessing import Queue

task_queue=Queue()
result_queue=Queue()            #创建发送任务和接收结果的队列，队列就像快递车

def get_task_queue():
    return task_queue

def get_result_queue():
    return result_queue    #windows无法直接使用lambda函数，因为无法对lambda函数进行序列化，所以只能定义一个函数来返回队列对象

class QueueManager(BaseManager):
    pass

QueueManager.register('task_queue',callable=get_task_queue)
QueueManager.register('result_queue',callable=get_result_queue)
#把创建的两个队列注册到网络上，允许其它进程通过网络访问，两个参数分别是名字和访问方法，名字相当于队列在网络上的名字，访问方法就是如何找到这个对象的方法
#调用的时候前参路牌后参路，先看路牌再走路
if __name__=='__main__':
    manager=QueueManager(address=('192.168.100.103',5000),authkey=b'abc')                
    #监听ip和端口，设置访问密码,任何进程都要通过这个ip和端口才能访问
    #创造一个QueueManager对象，QueueManager是BaseManager的子类，BaseManager提供了很多方法，QueueManager继承了这些方法
    manager.start()              #启动QueueManager，start表明这是Master，connect表明是Worker

    task=manager.task_queue()             
    #通过网络访问QueueManager的对象，调用之前注册的方法创建一个Queue对象，注意这个Queue对象不是本地的，而是通过网络访问到的Queue对象
    #因为QueueManager只开了内网接口，所以本机发送信号到路由，由路由转发到本机的Queue对象
    result=manager.result_queue()           #同上

    for i in range(10):
        n=random.randint(0,1000)
        print(f'将整数{n}放入任务队列...')
        time.sleep(1)
        task.put(n)
    time.sleep(2)
    print('尝试从结果队列获取结果...')
    for i in range(10):
        r=result.get(timeout=10)      #从结果队列获取结果，get方法会一直等待直到拿到结果，timeout参数设置10秒钟，如果10秒钟还没有拿到结果就报错
        print(f'第{i+1}个结果是{r}')
    #task传递关键数据，result获得处理过后的数据