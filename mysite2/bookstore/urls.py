from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("add_book/", views.add_book, name="add_book"),
    path("show_all_books/", views.show_all_books, name="show_all_books"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
]
