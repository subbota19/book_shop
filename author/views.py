from abc import ABC

from django.shortcuts import render, redirect
from .models import Authors
from book.models import Books
from django.db.models import Func, Avg


class RoundNumber(Func, ABC):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 0)'


# Create your views here.
def select_author(request, id_author):
    author = Authors.objects.all().get(id=id_author)
    books = Books.objects.all().filter(author=author).annotate(
        total_rating=RoundNumber(Avg('comments__rating')))[:3]
    return render(request, 'author/select_author.html', {'author': author, 'books': books})
