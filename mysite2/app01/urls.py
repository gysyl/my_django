from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('orm/', views.orm, name='orm'),
    path('info/list/', views.info_list, name='info_list'),
    path('info/add/', views.info_add, name='info_add'),
    path('info/edit/<int:user_id>/', views.info_edit, name='info_edit'),
    path('info/delete/<int:user_id>/', views.info_delete, name='info_delete'),
]
