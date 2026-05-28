'''
requests是一个更强大的链接访问工具
我们不只是从网页上爬取信息还可以对网页数据进行修改和优化
所以本章笔记从两个角度，爬虫和调用api来讲解requests的应用
'''

__author__ = "伟大的小熊猫"


import requests


account_passward={'username':'admin','password':'123456'}
r=requests.post('http://127.0.0.1:5000/api/login',json=account_passward)
print(r.cookies.get_dict())    

# r=requests.get('http://127.0.0.1:5000/api/pictures')   #这个链接是在浏览器开发者工具中捕捉到的
# #在打开浏览器的时候，找到GET方法对应的url，我们可以用这个url来用程序调用api
# pictures = r.json()['pictures']
# print(f"\n当前有 {len(pictures)} 张图片:")
# for pic in pictures:
#     print(f"  ID: {pic['id']} - {pic['title']}")


# r=requests.delete('http://127.0.0.1:5000/api/pictures/2')
# print('删除图片成功')

# json={'title':'武侯祠','url':'https://vcg00.cfp.cn/creative/vcg/800/new/VCG211389208861.jpg','description':'四川武侯祠的红墙和树林'}
# r=requests.put('http://127.0.0.1:5000/api/pictures/7',json=json)
#替换图片成功

#-------------------下面，在访问的时候传入一些特殊参数，可以增强访问手段或者传递数据信息---------------------

# params={'key':'编程'}
# r=requests.get('https://search.bilibili.com/all',params=params)

# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0'}
# r = requests.get('http://127.0.0.1:5000/gallery', headers=headers)
# print(r.text)                          #登录之后才能模拟浏览器访问获取数据


cs=r.cookies.get_dict()
r = requests.get('http://127.0.0.1:5000', cookies=cs)
#z这已经算是成功了，cookie已经拿到了，但只会保存在程序中，不会保存在浏览器开发者工具中

#最后上传图片
#本地图片 → 上传到服务器 → 服务器生成URL → 浏览器通过URL访问
#这要求服务器有将图片一对一生成url的功能
#如果服务器没有该功能即使上传图片也无法显示出来
#我们的网站目前不具备这个功能，所以无法上传图片，这个操作改日再议

# if __name__ == "__main__":
    # print(r.encoding)        #字符编码格式决定以哪种方式显示，而储存格式决定以哪种结构传递数据
    # #原始数据 → 数据格式（结构化）→ 字符编码（字节化）→ 存储/传输
    # print('\n')
    # print(r.url)
    #print(r.text)     #返回文本内容，结构内容
    # print('\n')
    # print(r.headers)
    # #print(r.headers['Content-Type'])
    # print('\n')
    # #print(r.json()) #不是json结构自然不能用json来解码
    # #print(r.content)  #以二进制形式返回文本内容
    # print(r.cookies)
