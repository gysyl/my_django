# 电子书管理系统

基于Django开发的电子书管理系统，提供电子书管理、用户认证和下载记录等功能。

## 功能特性

### 用户管理
- 用户注册：新用户可以创建账户
- 用户登录：已注册用户可以登录系统
- 个人中心：用户可以查看个人信息和下载历史

### 电子书管理
- 电子书列表展示
- 电子书下载功能
- 下载记录追踪
- 管理员后台管理

## 项目结构
```
ebook_manager/
├── books/                 # 主应用
│   ├── migrations/       # 数据库迁移文件
│   ├── static/          # 静态文件
│   ├── templates/       # HTML模板
│   │   └── books/
│   │       ├── center.html    # 个人中心页面
│   │       ├── index.html     # 首页
│   │       ├── login.html     # 登录页面
│   │       └── register.html  # 注册页面
│   ├── admin.py         # 管理员配置
│   ├── apps.py         # 应用配置
│   ├── models.py       # 数据模型
│   ├── tests.py        # 测试文件
│   ├── urls.py         # URL路由配置
│   └── views.py        # 视图函数
├── ebook_manager/       # 项目配置目录
│   ├── settings.py     # 项目设置
│   ├── urls.py         # 主URL配置
│   ├── wsgi.py        # WSGI配置
│   └── asgi.py        # ASGI配置
├── media/              # 媒体文件目录
├── static/             # 静态文件目录
├── manage.py          # Django管理脚本
└── requirements.txt    # 项目依赖
```

## 数据模型

### Book（电子书）
- title: 书名
- author: 作者
- file: 电子书文件
- cover: 封面图片
- description: 书籍描述
- upload_time: 上传时间

### Reader（读者）
- user: 关联Django用户模型
- nickname: 昵称
- avatar: 头像

### DownloadRecord（下载记录）
- book: 关联电子书
- reader: 关联读者
- download_time: 下载时间

## 主要功能实现

### 视图函数
- index: 首页展示
- register: 用户注册
- login: 用户登录
- logout: 用户登出
- center: 个人中心
- download_book: 电子书下载

### URL路由
- /: 首页
- /register/: 注册页面
- /login/: 登录页面
- /logout/: 登出
- /center/: 个人中心
- /download/<int:book_id>/: 下载电子书

## 技术栈
- Django Web框架
- SQLite数据库
- HTML/CSS前端
- Django内置用户认证系统

## 环境要求
- Python 3.x
- Django
- Pillow (用于图片处理)

## 安装和运行

1. 创建并激活虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

2. 安装依赖
```bash
pip install django pillow
```

3. 数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

4. 创建超级用户（可选，用于访问管理后台）
```bash
python manage.py createsuperuser
```

5. 启动开发服务器
```bash
python manage.py runserver
```

访问 http://127.0.0.1:8000/ 即可使用系统

## 使用说明

1. 管理员功能
   - 访问 /admin 进入管理后台
   - 管理电子书：添加、修改、删除电子书
   - 管理用户：查看用户信息和下载记录

2. 用户功能
   - 注册/登录：新用户需要先注册账号
   - 浏览电子书：在首页查看所有可用电子书
   - 下载电子书：点击下载按钮获取电子书文件
   - 查看记录：在个人中心查看下载历史

## 注意事项

- 确保media目录具有适当的写入权限
- 建议在生产环境中使用更安全的数据库（如PostgreSQL）
- 注意配置DEBUG=False并更新SECRET_KEY在生产环境中
- 定期备份数据库和媒体文件

## 开发建议

- 遵循Django的MTV（Model-Template-View）架构
- 使用Django Forms进行表单验证
- 实现文件上传大小限制
- 添加用户权限控制
- 实现电子书搜索功能