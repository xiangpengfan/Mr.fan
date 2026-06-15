'''
下面介绍一些零散的常用方法
'''

__author__='伟大的小熊猫'

import sys
print(sys.executable)   #返回正在运行的python解释器的路径

import os
print(os.getcwd())     #返回执行当前文件的命令行的目录，程序工作的文件夹
print(os.path.abspath('.'))  #返回当前程序的绝对路径，程序所在的文件夹

print(__file__)        #获取包含当前文件文件名的完整路径

print(sys.argv)        #获取命令行参数，不包括命令参数
#python 常用的一些方法.py
#只会打印出['常用的一些方法.py']，不会包含命令参数python
