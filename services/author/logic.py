from abc import ABC

from book.models import Books
from author.models import Authors
from django.db.models import Func, Avg


class RoundNumber(Func, ABC):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 0)'


def logic_select_author(id_author):
    author = Authors.objects.all().get(id=id_author)
    books = Books.objects.all().filter(author=author).annotate(
        total_rating=RoundNumber(Avg('comments__rating')))[:3]
    return {'author': author, 'books': books}
