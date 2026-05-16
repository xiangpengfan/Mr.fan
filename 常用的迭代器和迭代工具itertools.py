'''
介绍一些常用的迭代器和常用的迭代工具
'''

__author__ = "伟大的小熊猫"

import itertools

def first_n_minus_1_items(x,N):
    return (x+1)/2<=N

def add_sign(it):
    num=1
    for n in it:
        if num%2==0:
            yield -4/n
        else:
            yield 4/n
        num+=1

def pi(N):

    odd_numbers=itertools.count(1,2)
    items=itertools.takewhile(lambda x: x<=2*N-1,odd_numbers)
    #items=itertools.takewhile(first_n_minus_1_items(N),odd_numbers)  #这样写为什么不行
    #因为takewhile需要的函数只能输入一个参数，而first_n_minus_1_items需要两个
    #我们需要先对first_n_minus_1_items进行改造，以下：
    #itertools.takewhile(partial(first_n_minus_1_items, N=N), odd_numbers)
    items_sign=add_sign(items)
    #print(list(items_sign))#为什么这里加上listreturn打印的就不准确了
    #因为迭代器是一次性的，print了return就没得用了
    return sum(items_sign)

#标准答案
def pi(N):
    odds = itertools.count(1, 2)                  # step 1
    first_n = itertools.islice(odds, N)           # step 2: 取前 N 项
    signs = itertools.cycle([1, -1])              # step 3: 正负交替
    #terms = (4 * sign / n for sign, n in zip(signs, first_n))  # step 3
    #这个太库拉，zip可以同时遍历两个序列，cycle可以添加正负号，两者结合一步到位
    terms = (4 * next(signs) / n for n in first_n)
    #每次循环都会产生next新值
    return sum(terms) 

if __name__ == '__main__':
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    assert 3.04 < pi(10) < 3.05
    assert 3.13 < pi(100) < 3.14
    assert 3.140 < pi(1000) < 3.141
    assert 3.1414 < pi(10000) < 3.1415
    print('测试通过')

