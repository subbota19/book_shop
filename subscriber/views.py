from django.shortcuts import render

from services.subscriber.logic import *


def account(request):
    dict_with_date = logic_account(request.session['user'])
    if request.method == 'POST':
        if request.POST.get('order'):
            dict_with_date['error'] = logic_account_order_book(request.POST, dict_with_date['user'],
                                                               dict_with_date['status'], dict_with_date['error'])
        if request.POST.get('delete'):
            logic_account_delete_book(request.POST, dict_with_date['user'])

    return render(request, 'account/account.html', dict_with_date)
