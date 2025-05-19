"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('page<int:page>/', views.page, name='page'),
    path('calc/<int:a>/<str:op>/<int:b>/', views.calc, name='calc'),
    path('search/', views.search, name='search'),
    path('sum/', views.sum, name='sum'),
    path('login/', views.login, name='login'),
    path('login2/', views.login2, name='login2'),
    path('test/', views.test_view, name='test'),
    path('mytemp/', views.mytemp_view, name='mytemp'),
    path('mycal/', views.mycal_view, name='mycal'),
    path('test_for/', views.for_view, name='for'),
    path('index_base/', views.index_view, name='index_base'),
    path('sport/', views.sport_view, name='sport'),
    path('news/', views.news_view, name='news'),

]
