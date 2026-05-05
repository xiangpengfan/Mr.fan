'''
一个识别邮箱地址的简单的测试
'''

__author__ = "伟大的小熊猫"

import re

def is_valid_email(addr):
    pattern = r'^[a-zA-Z0-9.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, addr):
        return True
    else:
        return False

def name_of_email(addr):
    # pattern=r'^([a-zA-Z0-9]+)@[a-zA-z0-9]+\.[a-zA-Z]{3}$'
    # pattern2=r'^[<]([a-zA-Z0-9 ]+)[>][a-zA-Z ]+@[a-zA-z0-9]+\.[a-zA-Z]{3}$'
    pattern=r'^([a-zA-Z0-9]+)@'
    pattern2=r'^[<]([a-zA-Z0-9 ]+)[>][a-zA-Z ]+@'   #这是优化过后的表达式，只需要输出名字，不需要判断邮箱地址了
    if re.match(pattern2, addr):cc
        return re.match(pattern2, addr).group(1)
    else:
        return re.match(pattern, addr).group(1)     #把不同的邮箱地址的用户名按照不同的正则表达式提取出来，返回用户名


if __name__ == '__main__':
    # assert is_valid_email('someone@gmail.com')
    # # print(is_valid_email('someonegmail.com'))
    # assert is_valid_email('bill.gates@microsoft.com')
    # assert not is_valid_email('bob#example.com')
    # #print(is_valid_email('bob#example.com'))
    # assert not is_valid_email('mr-bob@example.com')
    # print('ok')
#--------------------------------------------------
    assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
    assert name_of_email('tom@voyager.org') == 'tom'
    print('ok')
    #print(name_of_email('<Tom Paris> tom@voyager.org'))