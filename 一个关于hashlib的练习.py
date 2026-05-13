import hashlib,random


def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode('ascii'))
    return md5.hexdigest()

# def login(user,password):
#     md5=calc_md5(password)
#     if db[user]==md5:
#         return True
#     else:
#         return False

# db={}

def get_md5(s):
    return calc_md5(s)

# def register(username, password):
#     db[username] = get_md5(password + username + 'the-Salt')

class User(object):
    def __init__(self,username,password):
        self.username=username
        self.salt=''.join([chr(random.randint(48,122)) for i in range(20)])
        #chr(...)：把整数转换成对应的 ASCII 字符,所以整个列表生成式所表达的意思是
        #生成一个又20个随机在48-122中的字符组成的字符串列表，然后把列表中的字符串连成一个
        self.password=get_md5(password+self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')             #用户名，密码，盐都已经确定了
}

def get_md5(user, pws):
    return calc_md5(pws+user.salt)          #用盐加上密码确定一下
    
def login(username, password):
    
    user = db[username]
    return user.password == get_md5(user, password)     
    #因为盐是确定的，加盐后的密码也是确定的，
    #直接用加盐密码的哈希和密码+盐的哈希进行比较
    #如果密码正确，返回True；否则返回False


if __name__ == '__main__':
    # assert login('michael', '123456')
    # assert login('bob', 'abc999')
    # assert login('alice', 'alice2008')
    # assert not login('michael', '1234567')
    # assert not login('bob', '123456')
    # assert not login('alice', 'Alice2008')
    # print('测试通过')
    # md5=calc_md5('123456')
    # print(md5)
   

    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('测试通过') 