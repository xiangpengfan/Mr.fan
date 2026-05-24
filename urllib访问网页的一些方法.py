'''
这里面有4种访问网页的方法，每一种都会使我们绕过一种网页的限制，实际使用过程中
通常配合使用
'''

__author__="伟大的小熊猫"

from urllib import request,parse
import io,gzip,json

# #直接访问 urlopen
# with request.urlopen('https://www.python.org') as f:
#     data=f.read()  #读取数据
#     print('状态，',f.status,f.reason)  #获取状态码和状态码对应的含义
#     for k,v in f.getheaders():    #获取数据的响应头，响应头：主体数据的配置信息
#         print(f'{k}:{v}')
#     try:
#         print('主题数据：',data.decode('utf-8'))
#     except UnicodeDecodeError:
#         buf = io.BytesIO(data)
#         with gzip.GzipFile(fileobj=buf,mode='rb') as f2:
#             print('主题数据：',f2.read().decode('utf-8'))
#         #GzipFile(fileobj=数据文件,mode='操作方式') 用来解压数据的一个类


# #通过增加标头来模拟用户访问：访问器request.Request
# r=request.Request('https://www.python.org')  #创建一个访问器，可以伪装成普通用户来访问
# r.add_header('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0')
# #模拟Microsoft Edge浏览器发送时的User-Agent信息,可以去浏览器开发者工具中查询，Fn+F12打开开发者工具---->network网络---->请求标头---->User-Agent
# with request.urlopen(r) as f:
#     data=f.read()
#     print('状态，',f.status,f.reason)
#     for k,v in f.getheaders():
#         print(f'{k}:{v}')
#     try:
#         print('主体数据：',data.decode('utf-8'))
#     except UnicodeDecodeError:
#         buf=io.BytesIO(data)
#         with gzip.GzipFile(fileobj=buf,mode='rb') as f2:  #把二进制压缩文件解压
#             print('主体数据：',f2.read().decode('utf-8'))
# #后面这部分是普通的访问代码


# #访问需要账号密码的登录页
# print('以微博为例，模拟需要密码的登录页如何抓取数据')
# email=input('请输入账号:')     #'https://passport.lanqiao.cn/api/v1/login/?auth_type=login'登录接口也要找
# passwd=input('请输入密码:')
# login_data=json.dumps(
#     {
#         'login_str':email,
#         'password':passwd,
#         'usertype':0
#     }
# ).encode('utf-8')

# login_url='https://passport.lanqiao.cn/api/v1/login/?auth_type=login'
 
# req=request.Request(login_url,data=login_data)     #创建一个访问器,模拟浏览器访问
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0')
# req.add_header('Referer','https://www.lanqiao.cn/login')
# req.add_header('Origin','https://www.lanqiao.cn')
# req.add_header('Content-Type','application/json')

# try:
#     with request.urlopen(req) as f:
#         print('Status:',f.status,f.reason)
#         for k,v in f.getheaders():
#             print(f'{k}:{v}')
        
#         data=f.read()
#         if f.getheader('Content-Encoding') == 'gzip':
#             buf = BytesIO(data)
#             with gzip.GzipFile(fileobj=buf, mode='rb') as gz:
#                 data = gz.read()
        
#         print('Data:', data.decode('utf-8'))
# except:
#     print('登录失败')

# #登录失败，因为没有动态参数nonce_id，这个参数是自动生成的，无法实现定义，可能需要使用 Selenium/Playwright，直接操作浏览器


def fetch_data(url):
    req=request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0')
    with request.urlopen(req) as f:
        data=f.read().decode('utf-8')
        return json.loads(data)

if __name__ == '__main__':
    URL = 'https://api.weatherapi.com/v1/current.json?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'
    data = fetch_data(URL)
    print(data)
    assert data['location']['name'] == 'Beijing'
    print('测试成功')