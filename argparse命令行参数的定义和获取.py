'''
这是一个简单的关于命令行参数定义和捕获的测试
定义数据库的命令行参数
目的备份数据库中的数据，这是第一步捕获命令行参数
数据库选择mysql
'''

__author__ = "伟大的小熊猫"




import argparse
def test():
    args=argparse.ArgumentParser(
        #这三个都是固定格式
        prog='一个测试程序',#program程序的名字
        description='一个简单的测试程序',#description描述信息
        epilog='2026.5.10'
    ) #生成一个命令行解析器

    args.add_argument('outfile')
    #定义一个位置参数，命令行中的值通过相对位置来寻找对应参数
    args.add_argument('--host',default='localhost')
    #定义一个关键词参数，命令行中的值通过--host来寻找对应参数
    args.add_argument('--port',type=int,default='3306')
    #同上，类型为整数，自动把捕获的值转换成整数
    args.add_argument('-u','--user',required=True)
    #require=True表示这个参数必须有值
    args.add_argument('-p','--password',required=True)
    args.add_argument('-d','--database',required=True)
    #这是数据库的名字
    args.add_argument('-gz','--gzcompress',action='store_true',help='通过gzip压缩备份文件')
    #action='store_true'表示这个参数不需要值，写了就是True，没写就是False

    namespace=args.parse_args()
    print(namespace)
    print(namespace.outfile)
    print(namespace.host)
    print(namespace.port)
    print(namespace.user)
    print(namespace.password)
    print(namespace.database)
    print(namespace.gzcompress)

    return


if __name__=='__main__':
    test()
