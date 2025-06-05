from django.http import HttpResponse
from django.shortcuts import render,redirect 
from app01.models import UserInfo, Department

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "app01/login.html")
    
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    if username == "admin" and password == "123":
        return redirect("https://www.baidu.com")
    
    return render(request, "app01/login.html", {"error_msg": "用户名或密码错误！"})
    
def orm(request):
    #models.Department.objects.create(title="研发部", location="上海")
    #models.Department.objects.create(title="市场部", location="北京")
    #models.Department.objects.create(title="人事部", location="广州")

    #UserInfo.objects.create(username="admin", password="123456", age=30, email="admin@example.com")
    #UserInfo.objects.create(username="user1", password="pass1", age=25, email="user1@example.com")
    
    # 查询所有用户信息
    users = UserInfo.objects.all()
    for user in users:
        print(user)
    # 查询特定用户
    specific_user = UserInfo.objects.get(username="admin")
    print(specific_user)
    # 更新用户信息
    #specific_user.age = 31
    #specific_user.save()
    # 删除用户信息
    #UserInfo.objects.filter(username="user1").delete()
    # 查询所有部门信息
    departments = Department.objects.all()
    for dept in departments:
        print(dept)
    return HttpResponse("ORM操作示例添加数据到数据库成功")  

def info_list(request):
    users = UserInfo.objects.all()
    return render(request, "app01/info_list.html", {"users": users})  
    
def info_add(request):
    if request.method == "GET":
        return render(request, "app01/info_add.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    if not username or not password:
        return render(request, "app01/info_add.html", {"error_msg": "用户名和密码不能为空！"})
    age = request.POST.get("age")
    email = request.POST.get("email")
    UserInfo.objects.create(username=username, password=password, age=age, email=email)
    from django.urls import reverse
    # 修正：始终使用反向url跳转，且表单action和跳转都用/app01/前缀
    return redirect(reverse("info_list"))

def info_edit(request, user_id):
    if request.method == "GET":
        user = UserInfo.objects.get(id=user_id)
        return render(request, "app01/info_edit.html", {"user": user})
    user = UserInfo.objects.get(id=user_id)
    user.username = request.POST.get("username")
    user.password = request.POST.get("password")
    user.age = request.POST.get("age")
    user.email = request.POST.get("email")
    user.save()
    from django.urls import reverse
    # 修正：始终使用反向url跳转，且表单action和跳转都用/app01/前缀
    return redirect(reverse("info_list"))

def info_delete(request, user_id):
    user = UserInfo.objects.get(id=user_id)
    user.delete()
    from django.urls import reverse
    # 修正：始终使用反向url跳转，且表单action和跳转都用/app01/前缀
    return redirect(reverse("info_list"))