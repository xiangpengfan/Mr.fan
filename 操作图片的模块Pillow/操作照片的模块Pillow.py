'''
Pillow允许我们对图片加滤镜、裁剪、旋转、调色、切片等等一系列操作，同时包含画笔功能，允许我们从零绘图

是一个非常好用的图片处理工具
'''


__author__ = '伟大的小熊猫'

from PIL import Image,ImageFilter,ImageDraw,ImageFont    #导入Pillow，但是导入的时候应该写PIL，历史原因
import random

# im=Image.open('VCG211394349551.jpg')  #导入图片
# w,h=im.size                           #获取图片的宽和高
# print(f'图片的宽度是{w},高度是{h}')    
# im.thumbnail((w/2,h/2))               #缩放，这里thunbnail接收到的是一个元组
# print(f'缩小后的宽度是{w/2},高度是{h/2}')
# im.save('缩略图.jpg')                 #保存，保存至当前文件夹



# im=Image.open('VCG211394349551.jpg')
# im2=im.filter(ImageFilter.BLUR)
# im2.save('模糊处理的图.jpg')

def random_char():
    return chr(random.randint(65,90))   #生成随机大写字母A-Z

def random_color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))  
    #目前还是数，配合RGB生成随机颜色，64-255排除了RGB中较暗的颜色

def random_color2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
    #32-127偏暗柔和

#下面我们创建一个画布，然后在画布上面写字母
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))  #创建一个画布
image.save('空白画布.jpg')

draw=ImageDraw.Draw(image)                           #创建一个只在特定画布写字的画笔
font=ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',36)          #创建一个字体格式，画笔可以根据对应的字体格式写出字体
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=random_color())          #给画布的每一个像素上色
image.save('上色画布.jpg')

for t in range(4):
    draw.text((60*t+10,10),random_char(),font=font,fill=random_color2())
image.save('写字画布.jpg')

image=image.filter(ImageFilter.BLUR)

image.save('写完字的模糊画布.jpg')
print('已生成最终画布')
