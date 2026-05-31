'''
这是一个简单的绘图模块，使我们绘图变得更简单
'''

__author__="伟大的小熊猫"

from turtle import *

# width(4)               #设置笔刷宽度
# forward(200)           #向前绘制200个像素，起点是原点，默认方向是正右
# #turtle原点再图形的正中间

# right(90)              #右转90度
# pencolor('red')        #设置笔刷颜色为红色
# forward(100)           #向前绘制100个像素

# right(90)              #右转90度
# pencolor('blue')       #设置笔刷颜色为蓝色
# forward(200)           #向前绘制200个像素

# right(90)              #右转90度
# pencolor('green')      #设置笔刷颜色为绿色
# forward(100)           #向前绘制100个像素

# done()                 #保持图片持续存在

#一会可以考虑写一下自己的名字

# #五星红旗
# color('red')
# penup()
# goto(-120,80)
# pendown()

# begin_fill()
# forward(240)
# right(90)
# forward(160)
# right(90)
# forward(240)
# right(90)
# forward(160)
# end_fill()


# penup()
# goto(-104,48)
# pendown()
# rt(90)

# color('yellow')
# for i in range(5):
#     forward(45)
#     right(144)

# penup()
# goto(-24,24)
# pendown()
# seth(0)

# for i in range(5):
#     forward(16)
#     right(144)


# penup()
# goto(-24,48)
# pendown()
# seth(30)

# for i in range(5):
#     forward(16)
#     right(144)

# penup()
# goto(-48,60)
# pendown()
# seth(60)

# for i in range(5):
#     forward(16)
#     right(144)

# penup()
# goto(-48,12)
# pendown()
# seth(-30)

# for i in range(5):
#     forward(16)
#     right(144)

# done()


##画一个分形树
colormode(255)    #设置颜色模式，默认RBG
#颜色模式可以理解为调色盘
lt(90)

lv=14
l=120
s=45

width(lv)         #设置笔刷宽度

r=0
g=0
b=0
pencolor(r,g,b)   #从调色盘中选颜色

penup()
bk(l)
pendown()
fd(l)             #画一个树干

def draw_tree(l,level):
    global r,g,b
    w=width()

    width(w*3/10)
    r=r+1
    g=g+2
    b=b+3
    pencolor(r%200,g%200,b%200)   #调正画笔画下一条线的颜色和宽度

    l=3.0/4.0*l                   #调整下一条线的长度

    lt(s)
    fd(l)                         #画下一条线

    if level<lv:
        draw_tree(l,level+1)      #这里循环的前代码是一条线，后面是一个分叉树，这个歪曲的分叉树就是这个迭代的模型
    bk(l)
    rt(2*s)
    fd(l)                         #画分叉树的另一条线

    if level<lv:
        draw_tree(l,level+1)      #这里循环的前代码是一个分叉树，所以它的迭代模型就是一个分叉树
    #这个迭代再上一个迭代之中，所以这个迭代主要是为了补全分叉
    bk(l)
    lt(s)
    width(w)                      #迭代的每一层恢复画笔的宽度


speed('fastest')
draw_tree(l,4)

done()