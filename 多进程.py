# from multiprocessing import Process
# import os

# def run_proc(name):
#     print(f'运行初始化进程{name}，初始化进程id为{os.getpid()}')

# if __name__=='__main__':
#     print(f'父进程{os.getpid()}')
#     p=Process(target=run_proc,args=('test',))
#     p.start()
#     p.join()
#     print('初始化进程结束')
#这些代码创建了一个临时的子进程对象，调用start（）方法后，子进程开始运行

# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
#     print(f'运行任务是{name},pid={os.getpid()}')
#     start=time.time()
#     time.sleep(random.random()*5)
#     end=time.time()
#     print(f'任务{name}运行时间{end-start:.2f}秒')

# if __name__=='__main__':
#     print(f'父进程{os.getpid()}')     #父进程就是本机进程
#     p=Pool(2)
#     for i in range(6):
#         p.apply_async(long_time_task,args=(i+1,))
#     print('等待所有子进程完成')
#     p.close()   
#     p.join()     #主进程等待进程池完成任务再继续代码运行
#     print('所有子进程完成') 
#这些代码创建了一个进程池，当我们需要创建大量的重复进程时，进程池是更好的选择
#我们只需要一组启动关闭代码，就可以管理很多进程，内存使用效率变高同时使我们的代码更为简洁

# import subprocess

# # print('打开执行程序nslookup，执行www.python.org命令')
# # r=subprocess.call(['nslookup','www.python.org'])
# # print('Exit code:',r)

# print('打开执行程序nslookup')
# p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# #output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
# output,err=p.communicate(b'www.python.org\nexit\n')
# print(output.decode('gbk'))
# print('退出代码：',p.returncode)
#这些代码创建了一个永久性的子进程

from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print(f'子程序的pid是{os.getpid()}')
    for value in ['才华','专业','核心']:
        print(f'将{value}放入队列。。。')
        q.put(value)
        time.sleep(random.random())

def read(q):
    print(f'子进程的pid是{os.getpid()}')
    while True:
        value=q.get(True)
        print(f'从队列取出{value}。。。')

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()        #因为有time.sleep(),所以子进程read()先读完q中的数据，父进程才结束其进程