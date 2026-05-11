'''
base64是把二进制数据转化成可读的字符串
'''
import base64,re

base64.b64encode(b'binary\x00string')
base64.urlsafe_b64encode(b'cahiisawbbcii') #将二进制编码成字符串

base64.b64decode('YmluYXJ5AHN0cmluZw==')
base64.urlsafe_b64decode('Y2FoaWlzYXdiY2NpaQ==')#将字符串解码成二进制数据

def safe_base64_decode(s):
    n=len(s)%4
    n=4-n
    if n!=4:
        while n-1>=0:
            s=s+'='
            n-=1
        return base64.b64decode(s.encode('ascii'))
    else:
        return base64.b64decode(s.encode('ascii'))
    
#下面是标准答案
def safe_base64_decode2(s):
    n=len(s)%4
    if n!=0:
        s=s+'='*(4 - n)  
        #if和while合并，用算数逻辑来减少代码逻辑
        #符号还可以乘数字
    return base64.b64decode(s.encode('ascii'))

def safe_base64_decode3(s):
    return base64.b64decode(s + '=' * (-len(s) % 4))
#(-len(s) % 4)==4-len(s)%4
#余数是多了几个，加上负号就变成了差几个可以补满


if __name__ == '__main__':
    # print(type(base64.b64encode(b'binary\x00string')))
    # print(base64.urlsafe_b64encode(b'cahiisawbbcii')) #将二进制编码成字符串

    # print(base64.b64decode('YmluYXJ5AHN0cmluZw=='))
    # print(base64.urlsafe_b64decode('Y2FoaWlzYXdiY2NpaQ=='))#将字符串解码成二进制数据

    # print(safe_base64_decode('YWJjZA=='))
    # print(safe_base64_decode('YWJjZA'))
    # print(base64.b64encode(b'abcd'))
    # print(base64.b64decode(b'YWJjZA=='))
    assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
    print('ok')
    print((-5 % 4))