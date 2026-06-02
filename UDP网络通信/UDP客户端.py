'''
这是遵循UDP通信协议的socket的客户端
'''

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#建立一个UDP套接字对象
while True:
    try:
        i=int(input('请输入要处理的数字：'))
        break
    except:
        print('请输入一个整数')
        continue
s.sendto(str(i).encode('utf-8'),('127.0.0.1',9999))
#向服务器发送数据
for i in range(3):
    data,addr=s.recvfrom(1024) #一个recfrom只能接收一次数据
    #接收数据
    print(data.decode('utf-8'))
s.close