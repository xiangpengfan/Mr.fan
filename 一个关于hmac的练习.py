'''
hamc用来生成随机的字符串salt，用数据+salt来生产哈希值，达到给数据加密的目的
这个过程叫加盐
传统的哈希
获得生成器------>生成hash值------>hexdigest()获取哈希值
hmac
获得加盐的生成器------>生成带盐的hash值------>hexdigest()获取哈希值
'''

__author__ = '__伟大的小熊猫__'


import hmac,random

def hasd_add_salt(message,key):
    message=message.encode('utf-8')
    key=key.encode('utf-8')   #生成哈希值必须是bytes字节文件
    h=hmac.new(key,message,digestmod='MD5')#直接生成哈希值
    #等效于
    # h=hmac.new(key,digestmod='MD5')
    # h.update(message)          #先生成加盐的生成器再生成哈希值
    return h.hexdigest()


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()
    #原始的是盐和数据加在一块然后算出来哈希，现在这个是数据和盐分开，一起输入算出哈希

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

if __name__ == '__main__':
    message='hello world'
    key='secret'
    print(hasd_add_salt(message,key))
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')