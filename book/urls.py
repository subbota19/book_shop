from django.urls import path, include
from .views import order_books, select_book,all_books

urlpatterns = [
    path('books_image', order_books, name="books_image"),
    path('select_book/page-<int:id_book>', select_book, name="select_books"),
    path('all_books', all_books, name="all_books"),
]
