'''
mvc是一种前后端分离的技术，关键点在于文件架构和数据传输方法
'''

__author__="伟大的小熊猫"

from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='范先生' and password=='258456fan':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='请输入正确的用户名和密码',username=username)

if __name__=='__main__':
    app.run(debug=True)