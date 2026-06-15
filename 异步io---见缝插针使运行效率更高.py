'''
asyncio和wait代表着进程的cpu运行速度的极致
就像一个工厂的工人，24小时不间断的干活，但是只是单个进程
如果想把计算机cpu发挥到极值，还需要多个进程
'''

__author__="伟大的小熊猫"

import asyncio,time

# async def main():
#     print('这是第一句')
#     await asyncio.sleep(1)
#     #只有间隔才可以设置await，而sleep不是间隔，是阻塞
#     print('这是第二句,不需要我写‘续’点，它自己会加入列表')
#     return '最后运行返回值'
# async def main2():
#     L=await asyncio.gather(main(),main(),main())
#     #这里必须设置await,固定格式
#     #因为不设置await,其它函数中的await就无法和它建立连接
#     #无法加入到待运行列表
#     print(L)


async def wget(host):
    print(f'正在访问{host}。。。')
    render,writer=await asyncio.open_connection(host,80)
    #这两个返回值是两个命令对象，一个负责读取，一个负责写入
    header=f'GET / HTTP/1.1\r\nHost:{host}\r\n\r\n'
    #构建http请求：“获取请求头”
    writer.write(header.encode('utf-8'))
    await writer.drain()

    while True:
        line=await render.readline()
        if line==b'\r\n':
            break
        print(f'{host}header > {line.decode("utf-8").strip()}')
    writer.close() 
    print(f'访问{host}结束')

async def main2():
    await asyncio.gather(wget('www.baidu.com'),wget('www.sina.com.cn'),wget('www.sohu.com'))




if __name__=='__main__':
    asyncio.run(main2())