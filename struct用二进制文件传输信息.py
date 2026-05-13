'''
解码一个bmp文件，然后返回图片大小颜色数
'''
import struct,base64
from collections import namedtuple


#获取bmp数据，两组
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

bmp_data=bmp_data[:30]

with open('bmp1.txt','rb') as f:
    bmp_data1=f.read(30)     #这个来模拟真实的场景




def bmp_info(date):
    d=struct.unpack('<ccIIIIIIHH',date)

    # bin=namedtuple('bin','width,height,color_used,color_important')# 创建一个容器模板，可以根据名称取值
    # bi=bin(d[6],d[7],d[8],d[9])
    #上面这个容器不行，我们需要一个字典

    if d[0]==b'B'and d[1]==b'M':
        return {'width':d[6],'height':d[7],'color_used':d[8],'color':d[9]}
    else:
        return print('不是bmp文件')

if __name__ == '__main__':
    # print(bmp_info(bmp_data)['width'])
    # bmp_info(bmp_data1)
    bi = bmp_info(bmp_data)
    assert bi['width'] == 28
    assert bi['height'] == 10
    assert bi['color'] == 16
    print('测试通过')
        