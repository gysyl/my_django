# Django 项目集合

这个仓库包含了多个Django项目，主要包括电子书管理系统（ebook_manager）、基础模板项目（myproject）和多应用示例项目（mysite1）。

## 主要项目：电子书管理系统 (ebook_manager)

### 项目描述
电子书管理系统是一个基于Django开发的Web应用，提供电子书的管理、用户注册登录、下载记录等功能。

### 主要功能
- 用户管理
  - 用户注册
  - 用户登录
  - 个人中心
- 电子书管理
  - 电子书列表展示
  - 电子书下载
  - 下载记录追踪

### 项目结构
```
ebook_manager/
├── books/                 # 主应用
│   ├── models.py         # 数据模型
│   ├── views.py          # 视图函数
│   ├── urls.py           # URL配置
│   └── templates/        # 模板文件
├── ebook_manager/        # 项目配置
└── manage.py            # Django管理脚本
```

### 技术栈
- Django Web框架
- SQLite数据库
- HTML/CSS前端

## 其他项目

### myproject
- 基础Django项目
- 包含多个模板示例
- 用于学习Django模板系统

### mysite1
- 多应用Django项目
- 包含bookstore、music、news等多个应用
- 展示了Django多应用架构

## 环境要求
- Python 3.x
- Django

## 安装和运行
1. 克隆仓库
2. 进入项目目录
3. 创建虚拟环境（推荐）
4. 安装依赖：`pip install django`
5. 运行迁移：`python manage.py migrate`
6. 启动服务器：`python manage.py runserver`

## 项目特点
- 模块化设计
- 完整的用户认证系统
- 清晰的代码结构
- 适合学习和参考的Django示例项目

## 注意事项
- 确保安装所有必要的依赖
- 在运行前完成数据库迁移
- 建议在开发环境中使用虚拟环境