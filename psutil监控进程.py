'''
psuil一个监控程序和系统信息运行信息的模块
py文件名称不要和模块名称相同
'''

__author__ = '伟大的小熊猫'

import psutil

#获取cpu信息  3个方法
# print(psutil.cpu_count())               #cpu的逻辑核数
# print(psutil.cpu_count(logical=False))  #cpu物理核数
# print(psutil.cpu_times())               #统计开机以来，各模式使用cpu的时间，单位是秒

#获取内存信息   2个方法

# print(psutil.virtual_memory())
# #svmem(total=16468996096, available=8473313280, percent=48.5, used=7995682816, free=8473313280)
# #total总内存,available可用内存,percent内存使用率,used已使用内存,free可用内存

# print(psutil.swap_memory())
# #sswap(total=1073741824, used=23445504, free=1050296320, percent=2.2, sin=0, sout=0)
# #total总内存,used已使用内存,free可用内存,percent内存使用率,sin从磁盘换入的内存累计量
# #sswap是备用内存官名虚拟内存的信息，内存不够用的时候从硬盘调的一部分储存空间


#获取磁盘信息   3个方法

# print(psutil.disk_partitions())    #磁盘的基本信息,默认扫描所有磁盘
# #[sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed')]
# #device磁盘名称,mountpoint访问路径,fstype文件系统类型,opts挂载选项
# #文件系统类型：你可以理解为文件系统储存文件的方式，它是在如何摆放文件
# #挂载选项：储存的文件允许的操作方式
# #rw读写,fixed硬盘不可移动，也就是固态硬盘;removable可移动硬盘

# print(psutil.disk_usage('/'))      #磁盘使用情况，'/'表示所有磁盘的使用情况
# #sdiskusage(total=214748360704, used=135941455872, free=78806904832, percent=63.3)
# #total总空间,used已使用空间,free可用空间,percent使用率

# print(psutil.disk_io_counters())   #磁盘IO信息，IO：储存和读取情况
# #sdiskio(read_count=379266, write_count=340159, read_bytes=16138114560, write_bytes=6206631424, read_time=204, write_time=135)
# #read_count读取次数,write_count写入次数,read_bytes读取字节,write_bytes写入字节,read_time读取时间,write_time写入时间

#获取本机网络信息 5个方法

#print(psutil.net_io_counters())    #获取网络IO信息
#snetio(bytes_sent=70585976, bytes_recv=273883171, packets_sent=214115, packets_recv=318533, errin=0, errout=1, dropin=0, dropout=0)
#bytes_sent发送的字节,bytes_recv接收的字节,packets_sent发送的数据包个数,packets_recv接收的数据包个数
#errin接收错误的数据包个数,errout发送错误的数据包个数,dropin接收时丢包个数,dropout发送时丢包个数

#print(psutil.net_if_addrs())    #获取网络接口信息,网卡信息，网卡：主机用来发送信息的出口
# info=psutil.net_if_addrs()
# for name, addresses in info.items():
#     print(f"\n{'='*50}")
#     print(f"【网卡名称】: {name}")
#     print(f"{'='*50}")
#     for addr in addresses:
#         # family 转成可读的文字
#         if addr.family == psutil.AF_LINK:
#             family_str = "MAC 地址 (物理地址)"
#         #elif addr.family == psutil.AF_INET6:
#             #family_str = "IPv6 地址"
#         else:
#             family_str = f"其他类型 ({addr.family})"
        
#         print(f"  {family_str}")
#         print(f"    地址:     {addr.address}")
#         if addr.netmask:
#             print(f"    子网掩码: {addr.netmask}")
#         if addr.broadcast:
#             print(f"    广播地址: {addr.broadcast}")

#print(psutil.net_if_stats())      #获取网络接口状态
# for name, infp in psutil.net_if_stats().items():
#     print(f"网卡名称：{name}")
#     print(f"状态：{infp.isup}")

#print(psutil.net_connections())     #获取网络连接信息
# n=0
# for conn in psutil.net_connections():
#     n=n+1
#     print(f'{"="*50}')
#     print(conn)
#     print(f'{"="*50}')
# print(f'一共有{n}个连接')

#获取进程信息  2个方法,一个是获取所有进程的信息，一个是获取指定进程的信息

print(psutil.pids())    #获取正在运行的进程ID


pid = 4
try:
    p = psutil.Process(pid)      #大方法里面有11个小方法
    print(f"成功连接进程 {pid}")
    
    # 逐个尝试并捕获异常
    try:
        print(f"名称: {p.name()}")
    except Exception as e:
        print(f"名称: 失败 ({e})")

    try:
        print(f"路径: {p.exe()}")    #返回进程的绝对路径
    except Exception as e:
        print(f"路径: 失败 ({e})")

    try:
        print(f"工作目录: {p.cwd()}")  #返回进程的工作路径，就是在哪里工作的
    except Exception as e:
        print(f"工作目录: 失败 ({e})")

    try:
        print(f"命令行: {p.cmdline()}")  #返回进程的命令行，对于自主运行的进程的命令行是上一级生成的
    except Exception as e:
        print(f"命令行: 失败 ({e})")

    try:
        print(f"父进程ID: {p.ppid()}")  #返回进程的父进程ID
    except Exception as e:
        print(f"父进程ID: 失败 ({e})")

    try:
        print(f"状态: {p.status()}") #返回进程的状态，运行或者未运行
    except Exception as e:
        print(f"状态: 失败 ({e})")

    try:
        print(f"用户名: {p.username()}")  #返回进程的用户名
    except Exception as e:
        print(f"用户名: 失败 ({e})")

    try:
        print(f"创建时间: {p.create_time()}") #返回进程的创建时间戳
    except Exception as e:
        print(f"创建时间: 失败 ({e})")

    try:
        print(f"内存信息: {p.memory_info()}") #返回进程的内存信息
    except Exception as e:
        print(f"内存信息: 失败 ({e})")

    try:
        print(f"网络连接: {p.connections()}")  #进程正在运行的网络连接
    except Exception as e:
        print(f"网络连接: 失败 ({e})")

    try:
        print(f"线程数: {p.num_threads()}")  #进程包含的线程数
    except Exception as e:
        print(f"线程数: 失败 ({e})")

except psutil.NoSuchProcess:
    print(f"PID {pid} 进程不存在")
except psutil.AccessDenied:
    print(f"无法访问 PID {pid}，即使以管理员身份运行也可能受限")