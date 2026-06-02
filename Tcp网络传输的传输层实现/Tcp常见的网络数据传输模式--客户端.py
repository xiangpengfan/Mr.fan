'''
tcp是requests的底层实现，这两个都是从网络上获取数据
如果是实际应用，其实更推荐requests
'''



import socket
import ssl

# ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ss.connect(('www.bilibili.com',443))
# context = ssl.create_default_context()  # 创建一个安全的上下文
# s = context.wrap_socket(ss, server_hostname="www.bilibili.com") 
# #现在都需要伪装一下，因为大多都是https链接而不是http


# s.send(b'GET / HTTP/1.1\r\nHost: www.bilibili.com\r\n"User-Agent: Mozilla/5.0\r\n"Connection: close\r\n\r\n')

# buffer=[]
# while True:
#     d=s.recv(4096)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data=b''.join(buffer)

# s.close()

# header,data=data.split(b'\r\n\r\n',1)

# print(header.decode('utf-8'))
# with open('ddps.html','wb') as f:
#     f.write(data)
#b站前端只有空白所以加载出来的也只是空白



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))  #接收欢迎信息

for data in ['小明'.encode('utf-8'),'小红'.encode('utf-8'),'小王'.encode('utf-8')]:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')

s.close
