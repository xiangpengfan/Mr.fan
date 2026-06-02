import socket,threading,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9999)) #绑定端口,两个参数一个是服务器的网关一个是服务器的端口号
s.listen(5)   #监听端口，这里最多排5个连接。。。
print('正在等待连接。。。')   #这是打印在服务器上的字符

def tcplink(sock,addr):
    print(f'接收来自{addr}的新连接')
    sock.send('欢迎访问我的服务器'.encode('utf-8'))
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(f'hello,{data.decode("utf-8")}!'.encode('utf-8'))
    sock.close()
    print(f'来自{addr}的连接已经关闭')

while True:
    sock,addr=s.accept()  #接收数据后返回一个新连接和地址
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()



    