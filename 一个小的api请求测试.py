from urllib import request
import json

url='https://www.freetogame.com/api/games'

#试发送请求
response=request.urlopen(url)         #urlopen(url)作用是发送请求
data=response.read().decode('utf-8')  #读取响应内容并解码

#正式发送请求
data=json.dumps({'key':'value'}).encode('utf-8')  #这是要发送的核心数据，并且数据已经经过编码
req=request.Request(url,data=data,headers={'Content-Type': 'application/json'})  #给核心对象进行包装，这是完整的可发送的数据包
response=request.urlopen(req)  #发送请求
result=response.read().decode('utf-8')  #读取响应内容并解码
for item in json.loads(result):  #将字符串转换为Python对象，并遍历每个元素
    print(str(item['id'])+' '+item['title']+' '+item['game_url'])  #打印每个元素的id和title字段
    if item['id']==39:
        print('找到id为39的游戏了！')
        print(json.dumps(item, indent=2, ensure_ascii=False))
# results=json.loads(result)  #将字符串转换为Python对象

# print(json.dumps(results, indent=2, ensure_ascii=False))  #以更美观的方式打印结果，indent=2表示每个层级缩进2个空格，ensure_ascii=False表示允许输出非ASCII字符（如中文）
