from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("add_book/", views.add_book, name="add_book"),
]
