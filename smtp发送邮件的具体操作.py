'''
作为传统通信的重要改版方式，电子邮件有着它独特的优势，具体来说有三个：
可靠性：电子邮件的延时性确保了它的可靠性，任何一封邮件内容往往都附带有完整的收发日志，可以直接作为证据被法院采用
兼容性：电子邮件的每一封邮件都可以直接对接程序，大型企业 OA、CRM、财务系统可以自动收发邮件生成工单，微信做不到程序自动收发消息。
接上/网站信息多是爬取，真正写程序如实时监控股票代码等还是需要邮件
开发性：收发电子邮件就像是在打电话，只需要知道对方的邮件地址就可以了，在跨国贸易和境外院校中有着不可替代的作用


下面我们将介绍smtp发送邮件的具体操作
需要了解的模块：smtplib和email
'''

__author__="伟大的小熊猫"


from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.utils import parseaddr,formataddr
from email.header import Header
from email.mime.text import MIMEText
import smtplib

#首先写一个文本邮件，以下是文本邮件的模板，模块选用MIMEText

# msg=MIMEText('<html><body><h1>你好</h1>' +
#     '<p>来自小熊猫的问候，小熊猫向您推荐了<a href="http://www.python.org">Python官网</a></p>' +
#     '</body></html>','html','utf-8')

# def __format_addr(s):
#     name,addr=parseaddr(s)
#     return formataddr((Header(name,'utf-8').encode(),addr))

# msg['Subject']=Header(' 思考有层次有深度，观点极具价值','utf-8').encode()
# msg['To']=__format_addr('范先生<fan2524994091@outlook.com>')
# msg['From']=__format_addr('小熊猫<18738073083@163.com>')




# server=smtplib.SMTP_SSL('smtp.163.com',465)     #25是名为发送，465是加密传输
# server.set_debuglevel(1)
# server.login('18738073083@163.com','QUiErin6a6GUwweW')
# server.sendmail('18738073083@163.com','fan2524994091@outlook.com',msg.as_string())
# server.quit()




#我们写一个多部分邮件，包括文本和图片和附件，模块选用MIMEMultipart
msg=MIMEMultipart()
def __format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

msg['Subject']=Header('审美格调高级，创作设计独具匠心','utf-8').encode()
msg['From']=__format_addr('小熊猫<18738073083@163.com>')
msg['To']=__format_addr('范先生<fan2524994091@outlook.com>')

#我们可以加载两个文本文件
#如果对方客户端无法接html就会接收文本格式
#如果对方客户端可以接收html和文本，就会优先发送第一个，另一个作为附件发送
msg.attach(MIMEText('<html><body><h1>向阳花木亦为春</h1>'+
'<p><img src="cid:0"></p>'+
'<p>我会优先给你发送这个邮件</p>'
'</body></html>','html','utf-8'))
msg.attach(MIMEText('如果对方客户端太陈旧，无法接收html格式，就会发送这封纯文本邮件','plain','utf-8'))

# #这里我们将会用两种模块分别来实现，MIMEImage和MIMEBase
# with open('D:/剪辑素材/视频素材/VCG211343392402.jpg','rb') as f:
#     mime=MIMEImage(f.read())
#     mime.add_header('Content-Disposition','attachment',filename='向阳花木亦为春')
#     msg.attach(mime)
# #MIMEImage使用起来非常方便，但他只针对图片

#这里我们将会用MIMEBase模块来实现相同的功能
with open('D:/剪辑素材/视频素材/VCG211343392402.jpg','rb') as f:
    mime=MIMEBase('image','jpg',filename='向阳花木亦为春')      #先创建一个骨架
    mime.add_header('Content-Disposition','attachment',filename='向日葵')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())    #把内容补充上去
    encoders.encode_base64(mime)  #把内容编码成二进制数据
    msg.attach(mime)


server=smtplib.SMTP('smtp.163.com',25)
server.starttls()         #创建smtp客户端对象后立刻接上starttls()方法，可以使信息加密传输
server.set_debuglevel(1)
server.login('18738073083@163.com','QUiErin6a6GUwweW')
server.sendmail('18738073083@163.com','fan2524994091@outlook.com',msg.as_string())
server.quit()