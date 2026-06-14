def consumer():
    r=''      #这个用来作为缓冲区
    while True:
        n=yield r                #在这里设置断点
        if not n:
            return
        print(f'[消费者]正在消费{n}。。。。')
        r='200 OK'

def producer(c):
    c.send(None)
    n=0
    while n<5:
        n+=1
        print(f'[生产者]生产者运行{n}。。。。')
        r=c.send(n)             #这里继续运行函数consumer，并进行交叉赋值
        #因为consumer是一个死循环，所以在send之后，代码会进入下一个yield等待
        print(f'[生产者]消费者返回{r}。。。。')
    c.close()

c=consumer()
producer(c)