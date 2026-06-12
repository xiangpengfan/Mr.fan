'''
WSGI已经可以实现单个url的处理，但是一个网站通常会有很多url，
在处理多url的时候，又有一些共用的代码逻辑可以抽象出来
把这些逻辑封装成一个工具包，这个工具包就是一个web框架

常见的共用逻辑有两种：路由判断和url类型的判断、orm框架的使用

今天了解的Flask就是一个web框架
'''

__author__="伟大的小熊猫"

from flask import Flask
from flask import request

app=Flask(__name__)     #创建命令对象

@app.route('/',methods=['GET','POST'])  #执行封装逻辑,route路线路径
def home():
    return '<h1>这是官网首页,访问内容请移步登录页</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return  '''<form action="/signin" method="post">
                <p><label>用户名:<input type="text" name="username"></label></p>
                <p><label>密码:<input type="password" name="password"></label></p>
                <p><input type="submit" value="登录"></p>
                </form>'''

@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>登录成功,欢迎管理员</h3>'
    return '<h3>账号或密码有误，请检查后重新输入</h3>'

if __name__=='__main__':
    app.run()