from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from services.book.logic import *

from django.db.models import Func
import json


class RoundNumber(Func, ABC):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 0)'


@csrf_exempt
def order_books(request):
    user = logic_select_book_get_user(request.session['user'])
    if not user.check_user_status():
        return redirect('sign_in')
    if request.method == 'POST':
        get_value = json.loads(request.body)
        logic_order_books_post(user, get_value)

    dict_with_date = logic_order_books(user)

    return render(request, 'home_page/content.html', dict_with_date)


@csrf_exempt
def select_book(request, id_book):
    dict_with_date = logic_select_book(request.POST, request.session['user'], id_book)
    return render(request, 'books/book.html', dict_with_date)


@csrf_exempt
def search_books(request):
    if request.method == 'POST':
        dict_with_date = logic_search_books(request.POST)
        return render(request, 'books/search_books.html', dict_with_date)
    return redirect('order_books')


def all_books(request):
    dict_with_date = logic_all_books()
    return render(request, 'books/all_books.html', dict_with_date)
