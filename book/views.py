from abc import ABC

from django.shortcuts import render, redirect
from .models import Books, Comments
from .models import Subscribers
from .form import CommentForm
from order.models import Orders, Status
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
from django.db.models import Func
import json


class RoundNumber(Func, ABC):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 0)'


@csrf_exempt
def order_books(request):
    user = Subscribers.objects.all().get(user_name=request.session['user'])
    if request.method == 'POST':
        get_value = json.loads(request.body)
        book = Books.objects.all().get(name=get_value)
        status = Status.objects.all().get(title='Новый')
        Orders(quantity=1, subscriber=user, book=book, status=status).save()

    if not user.check_user_status():
        return redirect('sign_in')
    new_book = Books.objects.all().order_by('created').reverse()[:4].annotate(
        total_rating=RoundNumber(Avg('comments__rating')))
    pop_book = Books.objects.all().annotate(total_rating=RoundNumber(Avg('comments__rating'))).order_by(
        'total_rating').reverse()[:4]
    return render(request, 'home_page/content.html',
                  {'new_book': new_book, 'pop_book': pop_book, 'user': request.session['user']})


@csrf_exempt
def select_book(request, id_book):
    book = Books.objects.all().annotate(total_rating=RoundNumber(Avg('comments__rating'))).get(id=id_book)
    user = Subscribers.objects.all().get(user_name=request.session['user'])
    comments = Comments.objects.all().filter(book=book)
    data = CommentForm(request.POST)
    if data.is_valid():
        Comments(description=data.cleaned_data['comment'], rating=data.cleaned_data['rating'],
                 subscriber=user, book=book).save()
    return render(request, 'books/book.html', {'book': book, 'comments': comments, 'form': CommentForm()})


def all_books(request):
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
    return render(request, 'books/all_books.html', {'books': all_book_with_slash})

# @receiver(request_started)
# def got_online(sender, **kwargs):
#     pass
#
#
# @receiver(request_finished)
# def got_offline(sender, **kwargs):
#     pass
#
