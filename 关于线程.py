# '''
# 下面模拟了一个多线程执行过程中可能会出错的那部分
# '''
# __author__='伟大的范先生'

# import threading,time
# from threading import Lock
# balance=0
# lock = threading.Lock()
# def change_balance(n):
#     global balance
#     balance=balance+int(n)
#     balance=balance-int(n)

# def run_thread(n):
#     with lock:
#         for i in range(10000000):
#             change_balance(n)

# if __name__=='__main__':
#     t1=threading.Thread(target=run_thread,args=(5,))
#     t2=threading.Thread(target=run_thread,args=(8,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(balance)


# '''
# 下面我们来写一些其他的线程测试
# '''
# __author__='伟大的范先生'

# import threading,multiprocessing

# print('当前CPU核的数量是：',multiprocessing.cpu_count())
# def loop():
#     x=0
#     while True:
#         x=x*1

# if __name__=='__main__':
#     for i in range(multiprocessing.cpu_count()):
#         t=threading.Thread(target=loop)
#         t.start()

# import multiprocessing

# def loop():
#     x=0
#     while True:
#         x=x*1

# if __name__=='__main__':
#     p=multiprocessing.Process(target=loop)
#     p.start()
#可以通过查看任务管理器的性能页面来查看，线程和进程使用内存的区别了

import time,threading

def loop():
    time.sleep(3)
    print(f'正在运行线程{threading.current_thread().name}')
    n=0
    while n<5:
        n=n+1
        print(f'线程{threading.current_thread().name}运行了{n}s')
        time.sleep(1)
    print(f'线程{threading.current_thread().name}停止运行')
    time.sleep(3)

if __name__=='__main__':
    print(f'当前线程是{threading.current_thread().name}')
    t=threading.Thread(target=loop,name='loopThread')
    t.start()
    t.join()
    print(f'当前线程{threading.current_thread().name}运行结束')