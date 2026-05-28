'''
带登录功能和图片管理的本地服务器
这是一个ai写的本地网站可以通过这个网站练习requests
首先要启动虚拟环境，然后运行这个文件，才能练习requests访问修改删除网站信息的操作
'''

from flask import Flask, request, jsonify, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'

# 模拟用户数据
USERS = {
    'admin': '123456',
    'test': 'password'
}

# 模拟图片数据（用字典存储，方便增删改）
PICTURES = {
    1: {
        'id': 1,
        'title': '🏔️ 山水如画',
        'url': 'https://picsum.photos/800/500?random=1',
        'description': '连绵起伏的山峦，清澈见底的湖水'
    },
    2: {
        'id': 2,
        'title': '🌲 森林秘境',
        'url': 'https://picsum.photos/800/500?random=2',
        'description': '阳光透过树叶洒下斑驳的光影'
    },
    3: {
        'id': 3,
        'title': '🌅 海边日落',
        'url': 'https://picsum.photos/800/500?random=3',
        'description': '金色的夕阳缓缓沉入海平面'
    },
    4: {
        'id': 4,
        'title': '🏛️ 古老城堡',
        'url': 'https://picsum.photos/800/500?random=4',
        'description': '中世纪城堡矗立在绿色的山丘上'
    }
}

# 用于生成新ID
next_id = 5

# 登录页面HTML（不变）
LOGIN_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>登录测试</title>
    <meta charset="utf-8">
    <style>
        body {
            font-family: Arial;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #f0f2f5;
            margin: 0;
        }
        .login-box {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            width: 350px;
        }
        h2 { text-align: center; color: #333; }
        input {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
            font-size: 14px;
        }
        button {
            width: 100%;
            padding: 12px;
            background: #1890ff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }
        button:hover { background: #40a9ff; }
        .message {
            text-align: center;
            margin-top: 15px;
            padding: 10px;
            border-radius: 4px;
            display: none;
        }
        .success { background: #f6ffed; color: #52c41a; display: block; }
        .error { background: #fff2f0; color: #ff4d4f; display: block; }
        .info {
            text-align: center;
            color: #999;
            font-size: 12px;
            margin-top: 20px;
            background: #fafafa;
            padding: 10px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>🔐 用户登录</h2>
        <form id="loginForm">
            <input type="text" id="username" placeholder="请输入用户名" required>
            <input type="password" id="password" placeholder="请输入密码" required>
            <button type="submit">登 录</button>
        </form>
        <div id="message" class="message"></div>
        <div class="info">
            📋 测试账号<br>
            admin / 123456<br>
            test / password
        </div>
    </div>

    <script>
        document.getElementById('loginForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const msgDiv = document.getElementById('message');
            
            try {
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ username, password })
                });
                
                const result = await response.json();
                
                if (result.status === 'success') {
                    msgDiv.className = 'message success';
                    msgDiv.textContent = result.message;
                    
                    setTimeout(() => {
                        window.location.href = '/gallery';
                    }, 1000);
                    
                } else {
                    msgDiv.className = 'message error';
                    msgDiv.textContent = result.message;
                }
                
            } catch (error) {
                msgDiv.className = 'message error';
                msgDiv.textContent = '网络错误，请确保服务器已启动';
            }
        });
    </script>
</body>
</html>
'''

# 风景画廊页面HTML（带增删改功能）
GALLERY_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>风景画廊 - 管理后台</title>
    <meta charset="utf-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            color: white;
            padding: 30px 0;
        }
        .header h1 { font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        
        .toolbar {
            max-width: 1200px;
            margin: 0 auto 30px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .btn {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            font-weight: bold;
            transition: all 0.3s;
            color: white;
        }
        .btn-add { background: #52c41a; }
        .btn-add:hover { background: #73d13d; transform: scale(1.05); }
        .btn-back { background: rgba(255,255,255,0.2); text-decoration: none; display: inline-block; }
        .btn-back:hover { background: rgba(255,255,255,0.4); }
        
        .gallery {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 25px;
            padding: 10px;
        }
        
        .card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            transition: transform 0.3s;
            position: relative;
        }
        .card:hover { transform: translateY(-8px); }
        
        .card img {
            width: 100%;
            height: 280px;
            object-fit: cover;
        }
        
        .card-content { padding: 20px; }
        .card-content h3 { color: #333; margin-bottom: 10px; font-size: 1.3em; }
        .card-content p { color: #666; line-height: 1.5; font-size: 14px; }
        
        .card-actions {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        
        .btn-edit { background: #1890ff; flex: 1; }
        .btn-edit:hover { background: #40a9ff; }
        .btn-delete { background: #ff4d4f; flex: 1; }
        .btn-delete:hover { background: #ff7875; }
        
        /* 模态框样式 */
        .modal {
            display: none;
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: rgba(0,0,0,0.6);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        .modal.active { display: flex; }
        
        .modal-content {
            background: white;
            padding: 30px;
            border-radius: 15px;
            width: 450px;
            max-width: 90%;
        }
        .modal-content h2 { margin-bottom: 20px; color: #333; }
        
        .form-group { margin-bottom: 15px; }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            color: #666;
            font-weight: bold;
        }
        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 14px;
            font-family: inherit;
        }
        .form-group textarea { height: 80px; resize: vertical; }
        
        .modal-actions {
            display: flex;
            gap: 10px;
            justify-content: flex-end;
            margin-top: 20px;
        }
        .btn-save { background: #52c41a; }
        .btn-cancel { background: #999; }
        .btn-save:hover { background: #73d13d; }
        .btn-cancel:hover { background: #b3b3b3; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🏞️ 风景画廊管理</h1>
        <p style="opacity:0.8; margin-top:10px;">你可以添加、修改或删除图片</p>
    </div>
    
    <div class="toolbar">
        <button class="btn btn-add" onclick="openAddModal()">➕ 添加新图片</button>
        <a href="/" class="btn btn-back">🔙 返回登录页</a>
    </div>
    
    <div class="gallery" id="galleryContainer">
        <!-- 图片卡片由JS动态生成 -->
    </div>
    
    <!-- 添加/编辑模态框 -->
    <div class="modal" id="editModal">
        <div class="modal-content">
            <h2 id="modalTitle">添加图片</h2>
            <input type="hidden" id="editId">
            <div class="form-group">
                <label>标题</label>
                <input type="text" id="editTitle" placeholder="请输入图片标题">
            </div>
            <div class="form-group">
                <label>图片URL</label>
                <input type="text" id="editUrl" placeholder="https://example.com/image.jpg">
            </div>
            <div class="form-group">
                <label>描述</label>
                <textarea id="editDesc" placeholder="请输入图片描述"></textarea>
            </div>
            <div class="modal-actions">
                <button class="btn btn-cancel" onclick="closeModal()">取消</button>
                <button class="btn btn-save" onclick="savePicture()">保存</button>
            </div>
        </div>
    </div>
    
    <script>
        // 加载所有图片
        async function loadPictures() {
            const response = await fetch('/api/pictures');
            const data = await response.json();
            
            const container = document.getElementById('galleryContainer');
            container.innerHTML = '';
            
            data.pictures.forEach(pic => {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <img src="${pic.url}" alt="${pic.title}" onerror="this.src='https://via.placeholder.com/800x500?text=图片加载失败'">
                    <div class="card-content">
                        <h3>${pic.title}</h3>
                        <p>${pic.description}</p>
                        <div class="card-actions">
                            <button class="btn btn-edit" onclick="openEditModal(${pic.id})">✏️ 修改</button>
                            <button class="btn btn-delete" onclick="deletePicture(${pic.id})">🗑️ 删除</button>
                        </div>
                    </div>
                `;
                container.appendChild(card);
            });
        }
        
        // 打开添加模态框
        function openAddModal() {
            document.getElementById('modalTitle').textContent = '➕ 添加新图片';
            document.getElementById('editId').value = '';
            document.getElementById('editTitle').value = '';
            document.getElementById('editUrl').value = '';
            document.getElementById('editDesc').value = '';
            document.getElementById('editModal').classList.add('active');
        }
        
        // 打开编辑模态框
        async function openEditModal(id) {
            const response = await fetch(`/api/pictures/${id}`);
            const data = await response.json();
            
            document.getElementById('modalTitle').textContent = '✏️ 修改图片';
            document.getElementById('editId').value = data.id;
            document.getElementById('editTitle').value = data.title;
            document.getElementById('editUrl').value = data.url;
            document.getElementById('editDesc').value = data.description;
            document.getElementById('editModal').classList.add('active');
        }
        
        // 关闭模态框
        function closeModal() {
            document.getElementById('editModal').classList.remove('active');
        }
        
        // 保存图片（添加或更新）
        async function savePicture() {
            const id = document.getElementById('editId').value;
            const data = {
                title: document.getElementById('editTitle').value,
                url: document.getElementById('editUrl').value,
                description: document.getElementById('editDesc').value
            };
            
            let response;
            if (id) {
                // 更新
                response = await fetch(`/api/pictures/${id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
            } else {
                // 新增
                response = await fetch('/api/pictures', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
            }
            
            if (response.ok) {
                closeModal();
                loadPictures();  // 刷新列表
            } else {
                alert('保存失败！');
            }
        }
        
        // 删除图片
        async function deletePicture(id) {
            if (!confirm('确定要删除这张图片吗？')) return;
            
            const response = await fetch(`/api/pictures/${id}`, {
                method: 'DELETE'
            });
            
            if (response.ok) {
                loadPictures();  // 刷新列表
            } else {
                alert('删除失败！');
            }
        }
        
        // 点击模态框外部关闭
        document.getElementById('editModal').addEventListener('click', function(e) {
            if (e.target === this) closeModal();
        });
        
        // 页面加载时获取图片列表
        loadPictures();
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    '''显示登录页面'''
    return render_template_string(LOGIN_HTML)

@app.route('/api/login', methods=['POST'])
def login():
    '''处理登录请求'''
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in USERS and USERS[username] == password:
        session['user'] = username
        return jsonify({
            'status': 'success',
            'message': f'✅ 欢迎回来，{username}！',
            'redirect': '/gallery'
        })
    else:
        return jsonify({
            'status': 'error',
            'message': '❌ 用户名或密码错误'
        }), 401

@app.route('/gallery')
def gallery():
    '''显示风景画廊页面'''
    if 'user' not in session:  # ✅ 没登录就跳回登录页
        return redirect('/')
    return render_template_string(GALLERY_HTML)

# ==================== 图片管理 API ====================

@app.route('/api/pictures', methods=['GET'])
def get_pictures():
    '''获取所有图片'''
    return jsonify({
        'pictures': list(PICTURES.values()),
        'total': len(PICTURES)
    })

@app.route('/api/pictures/<int:picture_id>', methods=['GET'])
def get_picture(picture_id):
    '''获取单张图片'''
    picture = PICTURES.get(picture_id)
    if picture:
        return jsonify(picture)
    return jsonify({'error': '图片不存在'}), 404

@app.route('/api/pictures', methods=['POST'])
def add_picture():
    '''添加新图片'''
    global next_id
    data = request.get_json()
    
    # 验证必填字段
    if not data.get('title') or not data.get('url'):
        return jsonify({'error': '标题和URL不能为空'}), 400
    
    new_picture = {
        'id': next_id,
        'title': data.get('title'),
        'url': data.get('url'),
        'description': data.get('description', '')
    }
    
    PICTURES[next_id] = new_picture
    next_id += 1
    
    return jsonify(new_picture), 201

@app.route('/api/pictures/<int:picture_id>', methods=['PUT'])
def update_picture(picture_id):
    '''修改图片'''
    if picture_id not in PICTURES:
        return jsonify({'error': '图片不存在'}), 404
    
    data = request.get_json()
    
    PICTURES[picture_id].update({
        'title': data.get('title', PICTURES[picture_id]['title']),
        'url': data.get('url', PICTURES[picture_id]['url']),
        'description': data.get('description', PICTURES[picture_id]['description'])
    })
    
    return jsonify(PICTURES[picture_id])

@app.route('/api/pictures/<int:picture_id>', methods=['DELETE'])
def delete_picture(picture_id):
    '''删除图片'''
    if picture_id not in PICTURES:
        return jsonify({'error': '图片不存在'}), 404
    
    deleted = PICTURES.pop(picture_id)
    return jsonify({'message': f'图片"{deleted["title"]}"已删除', 'id': picture_id})

@app.route('/api/users')
def get_users():
    '''获取用户列表'''
    return jsonify({
        'users': list(USERS.keys()),
        'total': len(USERS)
    })

@app.route('/api/logout')
def logout():
    session.pop('user', None)
    return jsonify({'message': '已退出登录'})

if __name__ == '__main__':
    print('=' * 50)
    print('🚀 图片管理服务器已启动！')
    print('📝 浏览器访问: http://127.0.0.1:5000')
    print('📋 测试账号: admin/123456 或 test/password')
    print('🖼️  登录后可添加、修改、删除图片')
    print('=' * 50)
    app.run(debug=True, host='127.0.0.1', port=5000)