'''
介绍一种传统的传递数据的媒介：xml
现在的情况下，我们通常只解包xml，不打包或者打包一些很简单的xml
'''

__author__="伟大的小熊猫"

from xml.parsers.expat import ParserCreate
from urllib import request

# class DefaultSaxHandler(object):
#     def start_element(self,name,attrs):
#         print(f'sax:初始标签：{name}，{str(attrs)}')
    
#     def end_element(self,name):
#         print(f'sax:结束标签：{name}')

#     def char_data(self,text):
#         print(f'sax:内容：{text}')
# #xml数据由三段构成，开始标签，内容，结束标签，先把处理这三段数据的函数写出来

# parser=ParserCreate() 
# #创建一个解析器，解析器可以把xml文本分为三部分，开始、内容、结束,但它无法返回数据并且无法对数据进行操作
# handler=DefaultSaxHandler()
# #创建一个处理函数，处理函数负责返回数据并对数据进行操作
# parser.StartElementHandler=handler.start_element
# parser.EndElementHandler=handler.end_element
# parser.CharacterDataHandler=handler.char_data

# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
# #注意：‘<ol>’‘<li>’‘<a href="/python">’都是初始标签
# #‘</a>’‘</li>’‘</ol>’都是结束标签
# #划分三段是对每一个初始标签和结束标签进行划分，而不是整体按顺序划分



#——————————————————————————————————————————
class DefaultSaxHandler(object):
    def __init__(self):
        self.name=''
        self.d={}
        self.d2={}
        self.button=False
    def start_element(self,name,attrs):
        self.name=name
        if name=='location':    
            self.button=True
    
    def end_element(self,name):
        if name=='location':
            self.button=False
        if name=='root':
            self.d['weather']=self.d2#这个赋值虽然写在了char_data前面，但是实际上是char_data执行完了才赋值的
            self.d2={}  
    def char_data(self,text): 
        if self.button and self.name=='name':         
            self.d['city']=text
        if self.name=='wind_kph':
            self.d2['wind']=float(text)
        if self.name=='temp_c':
            self.d2['temperature']=float(text)
        if self.name=='text':
            self.d2['condition']=text

#parseString等同于parser.Parse(xml_str)，了解任意一个创建解析器使用解析器够用



def parseXml(xml_str):
    parser=ParserCreate() 
    handler=DefaultSaxHandler()
    parser.StartElementHandler=handler.start_element
    parser.EndElementHandler=handler.end_element
    parser.CharacterDataHandler=handler.char_data

    parser.Parse(xml_str)
    h=handler.d    #这几个功能函数不能设置返回值，尝试从实例属性中获取结果
    handler.d={}
    return h


if __name__ == '__main__':
    URL = 'https://api.weatherapi.com/v1/current.xml?key=b4e8f86b44654e6b86885330242207&q=Beijing&aqi=no'

    with request.urlopen(URL, timeout=4) as f:
        data = f.read()

    result = parseXml(data.decode('utf-8'))
    #print(result)
    assert result['city'] == 'Beijing'
    print('测试通过')