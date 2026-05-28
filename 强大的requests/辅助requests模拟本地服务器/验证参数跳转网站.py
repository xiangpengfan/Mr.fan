from flask import Flask

# 创建网站应用
app = Flask(__name__)

# 创建第一个页面 - 首页
@app.route('/')
def home():
    return '''
    <h1>🎉 欢迎来到我的网站！</h1>
    <p>这是我的第一个本地网站</p>
    <a href="/hello">访问Hello页面</a>
    '''

# 创建第二个页面
@app.route('/hello')
def hello():
    return '<h1>Hello World!</h1><p>这是第二个页面</p>'

# 启动服务器
if __name__ == '__main__':
    print('=' * 50)
    print('🚀 服务器已启动！')
    print('📝 在浏览器打开: http://127.0.0.1:5000')
    print('=' * 50)
    app.run(debug=True, host='127.0.0.1', port=5000)