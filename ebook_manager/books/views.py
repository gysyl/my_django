

from django.shortcuts import render, redirect
from .models import Reader, Book, Category
from django.contrib import messages
from .models import Book, BookFile  # 导入模型


def index(request):
    # 获取所有分类和书籍
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        books = Book.objects.filter(category_id=category_id)
    else:
        books = Book.objects.all()
    return render(request, 'books/index.html', {
        'categories': categories,
        'books': books,
        'selected_category': int(category_id) if category_id else None,
    })

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not username or not password:
            messages.error(request, '用户名和密码不能为空')
            return render(request, 'books/register.html')
        if Reader.objects.filter(username=username).exists():
            messages.error(request, '用户名已存在')
            return render(request, 'books/register.html')
        Reader.objects.create(username=username, password=password, email=email)
        messages.success(request, '注册成功，请登录')
        return redirect('books_login')
    return render(request, 'books/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Reader.objects.filter(username=username, password=password).first()
        if user:
            request.session['reader_id'] = user.id
            request.session['reader_name'] = user.username
            return redirect('books_index')
        else:
            messages.error(request, '用户名或密码错误')
    return render(request, 'books/login.html')

def logout(request):
    request.session.flush()
    return redirect('books_login')

def center(request):
    if not request.session.get('reader_id'):
        return redirect('books_login')
    return render(request, 'books/center.html')


def category_list(request):
    # 获取所有分类（可选：预加载关联的书籍）
    categories = Category.objects.prefetch_related('book_set').all()  # 优化查询性能
    return render(request, 'books/category_list.html', {'categories': categories})


def upload_book(request):
    if request.method == "GET":
        # 渲染上传表单模板
        return render(request, 'books/upload_book.html')
    
    # 处理POST请求（用户提交表单）
    title = request.POST.get('title')
    author = request.POST.get('author')
    description = request.POST.get('description')
    category_id = request.POST.get('category')
    file = request.FILES.get('file')  # 获取上传的文件
    file_format = request.POST.get('file_format')  # 文件格式（需与BookFile.FORMAT_CHOICES一致）

    # 创建Book和BookFile记录
    if title and file:
        # 关联当前登录用户（假设用户已登录，从session获取reader_id）
        reader_id = request.session.get('reader_id')
        reader = Reader.objects.get(id=reader_id) if reader_id else None

        # 创建Book实例
        book = Book.objects.create(
            title=title,
            author=author,
            description=description,
            category_id=category_id,
            reader=reader  # 关联上传者
        )

        # 创建BookFile实例（保存上传的文件）
        BookFile.objects.create(
            book=book,
            file=file,  # 自动保存到settings.MEDIA_ROOT/books/目录
            file_format=file_format
        )

        # 上传成功后跳转回首页
        return redirect('books_index')  # 'books_index' 是首页的URL名称（需与urls.py一致）
    
    # 上传失败（字段缺失）
    return render(request, 'books/upload_book.html', {'error_msg': '请填写书名并选择文件'})