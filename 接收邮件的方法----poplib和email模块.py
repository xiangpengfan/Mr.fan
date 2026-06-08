'''
接收邮件的实现代码，邮件发送与接收非常重要，邮件的地位就非常重要
详情请参照发送邮件章节
'''

__author__='伟大的小熊猫'

import poplib
from email.parser import  Parser
from email.header import decode_header
from email.utils import parseaddr 

#接收邮件和发送邮件正好相反，接收邮件需要先把邮件下载到本地，再对邮件进行解析
#这里注意一点，邮件下载到本地和邮件接收进入客户端过程是一样的，都是MTA--->MUA
#也就是说客户端和本地这两个生态位是相同的
server=poplib.POP3('pop.163.com')   #连接到网易的pop3服务器
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8')) 
#打印调试信息打印欢迎信息，注意这里打印的欢迎信息是二级制编码形式

server.user('18738073083@163.com')
server.pass_('QUiErin6a6GUwweW')   #接收方的客户端邮箱地址和登录口令

num,size=server.stat()
print(f'邮件数量:{num};占用空间:{size}')
resp,mails,octets=server.list()
#resp:响应状态；mails：邮件列表信息；octets：所有的邮件总的内容信息
#这个函数负责打印出所有邮件的基本信息
print(mails)      #打印邮件列表信息，（序号，名称）

index=len(mails)
resp,lines,octets=server.retr(index)
#lines：每封邮件的具体内容拆分成一行一行的信息，组成一个列表
#retr自带循环，这个函数负责打印出每一封邮件的具体内容
msg_content=b'\r\n'.join(lines).decode('utf-8')
msg=Parser().parsestr(msg_content)
#只能还原邮件的结构，并进行二进制解码，但是无法完整还原邮件的内容
print(msg)

server.quit()


def print_info(msg,indent=0):
    if indent==0:                       #确保头部信息只被调用一次
        for header in ['From','To','Subject']:
            value=msg.get(header,'')   #获得头部信息的内容，如果没有打印空值
            if value:
                if header=='Subject':
                    value=decode_str(value)
                else:
                    hdr,addr=parseaddr(value)
                    name=decode_str(hdr)
                    value=f'{name} <{addr}>'
            print(f'{header}:{value}')
    if (msg.is_multipart()):
        parts=msg.get_payload()
        for n,part in enumerate(parts):
            print(f'{'  '*indent}{"-"*20}第{n+1}部分的内容{"-"*20}')#外层编号外层，内层编号内层，同缩进的层级逐次编号
            #文件通常的结构是第一部分是主体，主体中内容和图片分别是第一部分第二部分，第二部分是附件，第三部分是第二个附件
            print_info(part,indent+1)       #分别打印各部分内容
    else:
        content_type=msg.get_content_type()     #先获取内容类型
        if content_type=='text/plain' or content_type=='text/html':
            content=msg.get_payload(decode=True)          #这里获取内容的时候经过了一次解码
            charset=get_charset(msg)           #这里获取编码类型
            if charset:
                content=content.decode(charset) #通过编码进行第二次解码，带上parser解析时进行的一次解码，三次解码完成
            print(f'{'  '*indent}Text：{content}')
        else:
            print(f'{'  '*indent}附件：{msg.get_filename()}')

def decode_str(s):
    value,charset=decode_header(s)[0]
    if charset:
        value=value.decode(charset)
    return value

def get_charset(msg):
    charset=msg.get_charset()
    if charset is None:
        content_type=msg.get('Content-Type','').lower()
        pos=content_type.find('charset=')
        if pos>=0:
            charset=content_type[pos+8:].strip()
    return charset

if __name__=='__main__':
    #接收邮件和发送邮件正好相反，接收邮件需要先把邮件下载到本地，再对邮件进行解析
    #这里注意一点，邮件下载到本地和邮件接收进入客户端过程是一样的，都是MTA--->MUA
    #也就是说客户端和本地这两个生态位是相同的
    server=poplib.POP3('pop.163.com')   #连接到网易的pop3服务器
    server.set_debuglevel(1)
    print(server.getwelcome().decode('utf-8')) 
    #打印调试信息打印欢迎信息，注意这里打印的欢迎信息是二级制编码形式

    server.user('18738073083@163.com')
    server.pass_('QUiErin6a6GUwweW')   #接收方的客户端邮箱地址和登录口令

    num,size=server.stat()
    print(f'邮件数量:{num};占用空间:{size}')
    resp,mails,octets=server.list()
    #resp:响应状态；mails：邮件列表信息；octets：所有的邮件总的内容信息
    #这个函数负责打印出所有邮件的基本信息
    print(mails)      #打印邮件列表信息，（序号，名称）

    index=len(mails)
    resp,lines,octets=server.retr(index)
    #lines：每封邮件的具体内容拆分成一行一行的信息，组成一个列表
    #retr自带循环，这个函数负责打印出每一封邮件的具体内容
    msg_content=b'\r\n'.join(lines).decode('utf-8')
    msg=Parser().parsestr(msg_content)
    #只能还原邮件的结构，并进行二进制解码，但是无法完整还原邮件的内容
    # print(msg)

    # server.quit()
    print_info(msg,indent=0)