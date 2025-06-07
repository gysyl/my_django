from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books_index'),
    path('register/', views.register, name='books_register'),
    path('login/', views.login, name='books_login'),
    path('logout/', views.logout, name='books_logout'),
    path('center/', views.center, name='books_center'),
    path('categories/', views.category_list, name='category_list'),  # 之前添加的分类路由
    # 新增上传书籍路由
    path('upload/', views.upload_book, name='upload_book'),  # 关键修改！
]
