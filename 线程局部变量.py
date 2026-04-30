import threading
'''
线程没有self，这就导致在多层函数调用的过程中，参数没有传递的中介，所以就需要线程局部变量来解决这个问题
'''

local_school=threading.local()

def process_student():
    std=local_school.name
    age=local_school.age
    print(f'{std}成功加入了{threading.current_thread().name}线程,年龄是{age}')

def process_thread(name,age):
    local_school.name=name
    local_school.age=age
    process_student()

if __name__=='__main__':
    t1=threading.Thread(target=process_thread,args=('小明',20,),name='线程1')
    t2=threading.Thread(target=process_thread,args=('小王',26,),name='线程2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# 实际上我们线程局部变量解决的就是如何将变量传入线程中的函数的问题
# 如果我们在主进程中，要给函数传入一个变量，直接Global就可以了，但是在线程中，
# 它只能允许定义的时候输入几个参数，我们没有其它输入的空间，所以我们的一切操作只能在线程的参数
# 函数中进行，以下：
#     t1 = threading.Thread(target=参数函数，name='线程名称')
# 我们要在线程中把变量传入一个函数中，其实要解决的就两个问题：
# 1.变量的定义问题，在哪里定义变量                      #在参数函数中定义
# 2.变量的传递问题，怎么把变量传递到线程函数中去         #以更高层的容器为媒介  先传入容器再从参数函数传入到指定的函数
# Thread.local()底层就是这么运行的，它底层创建了一个字典容器，在参数函数中定义变量，
# 把变量放入这个字典容器中，在线程函数中通过这个字典容器来获取变量的值
# 并且，这个字典保存了线程的PID，以保证每个线程都能获取到自己定义的变量值

# 其实就相当于把函数拓展了类的self功能