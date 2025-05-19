"""
"""
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    index_html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我利用vscode创建的第一个页面</title>
</head>
<body>
    <h1>我利用vscode创建的第一个页面</h1>
    <p>这是我利用vscode创建的第一个页面,我希望在以后的学习中可以不断地完善它。</p>
    <a href="/search/?query=python&page=2">搜索 Python 第2页</a>
    <form action="/search/" method="get">
        <input type="text" name="query" value="django">
        <input type="number" name="page" value="1">
        <input type="submit" value="搜索">
    </form>
    
</body>
</html>
    """   
    return HttpResponse(index_html)

def page(request, page):
    return HttpResponse(f"你访问的是第 {page} 页")

def calc(request, a, op, b):
    try:
        if op == 'add':
            result = a + b
        elif op == 'sub':
            result = a - b
        elif op == 'mul':
            result = a * b
        elif op == 'div':
            if b == 0:
                return HttpResponse("除数不能为0", status=400)
            result = a / b
        else:
            return HttpResponse("无效操作符", status=400)

        return HttpResponse(f"{a} {op} {b} = {result}")

    except Exception as e:
        return HttpResponse(f"出错：{str(e)}", status=500)
    
def search(request):
    query = request.GET.get('query')
    page = request.GET.get('page')
    if not query:
        return HttpResponse("请输入搜索关键字", status=400)
    return HttpResponse(f"搜索关键词：{query}，第 {page} 页")  

def sum(request):
    # 从 GET 参数中获取 start、stop、step，默认值分别为 0, 0, 1
    try:
        start = int(request.GET.get('start', 0))  # 默认为 0
        stop = int(request.GET['stop'])           # stop 是必填项
        step = int(request.GET.get('step', 1))    # 默认为 1
    except (KeyError, ValueError):
        return HttpResponse("参数错误，请检查 start、stop、step 是否为整数")

    total = sum(range(start, stop, step))
    return HttpResponse(f"结果:{total}")


def login(request):
    login_form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>登录</title>
</head>
<body>
    <h1>登录</h1>
    <form action="/login/" method="post">
        <label for="username">用户名:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">密码:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <input type="submit" value="登录">
    </form>
</body>
</html>
"""
    if request.method == 'GET':
        return HttpResponse(login_form_html)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')      
        
        # 这里可以添加验证用户名和密码的逻辑
        return HttpResponse(f"登录成功，用户名: {username}, 密码: {password}")
    else:
        return HttpResponse(login_form_html)
    
def login2(request):
    context = {'name': '小明', 'password': '123456'}
    return render(request, 'mylogin.html', context)

def say_hello():
    return 'Hello,安怡'

class Dog:
    def say(self):
        return '汪汪汪'

def test_view(request):
    s = 'Hello, World!'
    lst = ['北京', '上海,', '深圳', '杭州', '成都', '西安', '广州']
    mydict = {'name': '小明', 'age': 18, 'gender': '男'}
    dic = {'s': s, 
           'lst': lst, 
           'mydict': mydict, 
           'say_hello': say_hello, 
           'dog1': Dog()
  }
    return render(request, 'test.html', dic)

def mytemp_view(request):
    #dic ={
    #    'x': 10,
    #}
    age = 19
    return render(request, 'mytemp.html',locals())

def mycal_view(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        op = request.POST.get('op')
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y 
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            if y == 0:
                return HttpResponse("除数不能为0", status=400)
            result = x / y
        else:
            return HttpResponse("无效操作符", status=400)

        return render(request, 'mycal.html', locals())
    
def for_view(request):
    s = 'Hello, World!'
    lst = ['北京', '上海', '深圳', '杭州', '成都', '西安', '广州']
    mydict = {'name': '小明', 'age': 18, 'gender': '男'}
    return render(request, 'for.html', locals())

def index_view(request):
    return render(request, 'base.html')  

def sport_view(request):
    return render(request, 'sport.html')

def news_view(request):
    return render(request, 'news.html')