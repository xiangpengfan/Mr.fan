'''
UDP是一个更快的通信模式，但是相较于TCP来说不太稳定
TCP正式通信前需要先建立通信通道
UDP通信直接发送接收数据，像两个客户端在对话
'''

import socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#建立一个UDP套接字对象
s.bind(('127.0.0.1',9999))  #绑定端口
print('UDP服务端已启动,连接端口9999.。。。。')
s.settimeout(15)

while True:
    data,addr=s.recvfrom(1024)   #接收数据
    print('接收到来自%s的数据:%s'%(addr,data))
    s.sendto('正在处理数据。。。。'.encode('utf-8'),addr)
    for i in range(3):
        time.sleep(1)
        print(3-i)
    data_num=int(data.decode('utf-8'))
    for i in range(data_num):
        if i==0:
            continue         #跳出本次循环循环，继续运行其它的循环 
        data_num=data_num*i
    s.sendto('数据处理完成'.encode('utf-8'),addr)
    print('数据处理完成')
    time.sleep(1)
    s.sendto(str(data_num).encode('utf-8'),addr)