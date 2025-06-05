

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from .models import MyUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = MyUser.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('myapp:user_center')
            else:
                error = "密码错误"
        except MyUser.DoesNotExist:
            error = "用户不存在"
        return render(request, 'myapp/login.html', {'error': error})

    return render(request, 'myapp/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if MyUser.objects.filter(username=username).exists():
            return render(request, 'myapp/register.html', {'error': '用户已存在'})

        MyUser.objects.create(username=username, password=make_password(password))
        return redirect('myapp:login')

    return render(request, 'myapp/register.html')

def user_center_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('myapp:login')

    user = MyUser.objects.get(id=user_id)
    return render(request, 'myapp/user_center.html', {'user': user})

def logout_view(request):
    request.session.flush()
    return redirect('myapp:login')
