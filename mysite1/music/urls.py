from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('page1/', views.page1),
    path('page2/', views.page2),
    path('page3/', views.page3),
]