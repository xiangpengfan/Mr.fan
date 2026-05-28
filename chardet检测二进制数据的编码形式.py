'''
chardet:一个检测二进制数据编码的模块
'''

__author__ = "伟大的小熊猫"


import chardet
data='だから俺は、諦めない！'.encode('utf-8')
data2='With great power comes great responsibility.'.encode('GBK')
#b"做人如果没梦想，那跟咸鱼有什么分别？"
data3="生活不是等待风暴过去，而是学会在雨中翩翩起舞。".encode('utf-8')
data4='离离原上草，一岁一枯荣'.encode('GBK')
#太短的数据可能有时候检测不准

print(chardet.detect(data4))   #'b'自动转二进制只能转成ascii形式
print('我运行了')