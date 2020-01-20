from abc import ABC

from book.models import Books, Comments
from subscriber.models import Subscribers
from book.form import CommentForm, Search
from order.models import Orders, Status

from django.db.models import Avg
from django.db.models import Func


class RoundNumber(Func, ABC):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 0)'


def logic_order_books(user):
    new_book = Books.objects.all().order_by('created').reverse()[:4].annotate(
        total_rating=RoundNumber(Avg('comments__rating')))
    pop_book = Books.objects.all().annotate(total_rating=RoundNumber(Avg('comments__rating'))).order_by(
        'total_rating').reverse()[:4]
    return {'new_book': new_book, 'pop_book': pop_book, 'user': user.user_name,
            'search_form': Search()}


def logic_order_books_post(user, get_value):
    book = Books.objects.all().get(name=get_value)
    status = Status.objects.all().get(title='Новый')
    if book.quantity:
        Orders(quantity=1, subscriber=user, book=book, status=status).save()


def logic_select_book_get_user(user):
    return Subscribers.objects.all().get(user_name=user)


def logic_select_book(request_POST, user, id_book):
    book = Books.objects.all().annotate(total_rating=RoundNumber(Avg('comments__rating'))).get(id=id_book)
    user = Subscribers.objects.all().get(user_name=user)
    comments = Comments.objects.all().filter(book=book)
    data = CommentForm(request_POST)
    if data.is_valid():
        Comments(description=data.cleaned_data['comment'], rating=data.cleaned_data['rating'],
                 subscriber=user, book=book).save()
    return {'book': book, 'comments': comments, 'form': CommentForm()}


def logic_search_books(request_POST):
    form = Search(request_POST)
    if form.is_valid():
        get_value = form.cleaned_data['search_string']
        book = Books.objects.all().filter(name__contains=get_value)
        return {'books': book, 'search_string': form.cleaned_data['search_string']}


def logic_all_books():
    books = Books.objects.all().annotate(total_rating=RoundNumber(Avg('comments__rating')))
    total = 0
    all_book_with_slash = []
    for book in books:
        all_book_with_slash.append(book)
        total += 1
        if total == 4:
            all_book_with_slash.append('/')
            total = 0
    # books = [x if list(books).index(x)+1 % 4 != 0 else [x, '/'] for x in books]
    return {'books': all_book_with_slash}

# @receiver(request_started)
# def got_online(sender, **kwargs):
#     pass
#
#
# @receiver(request_finished)
# def got_offline(sender, **kwargs):
#     pass
#
