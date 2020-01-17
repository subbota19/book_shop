from django.shortcuts import render, redirect
from subscriber.models import Subscribers
from order.models import Orders, Status


def account(request):
    user = Subscribers.objects.all().get(user_name=request.session['user'])
    orders = Orders.objects.all().filter(subscriber=user)
    status = Status.objects.all().get(title='Выполнен')
    error = ''
    if request.method == 'POST':
        if request.POST.get('order'):

            for book in request.POST.getlist('book'):
                first_orders = Orders.objects.all().filter(subscriber=user, book__name=book)
                for successful_order in first_orders:

                    if successful_order.status.is_active:

                        if successful_order.subscriber.cache >= successful_order.book.price:
                            error = 'The operation was a success'
                            user.all_buys += successful_order.book.total_price

                            user.cache -= (successful_order.book.total_price -
                                           successful_order.book.total_price * float(user.discount))
                            successful_order.status = status
                            successful_order.save()
                            user.save()
                        else:
                            error = "You don't have enough money for trading transactions in the account"
                            break

        if request.POST.get('delete'):
            for book in request.POST.getlist('book'):
                Orders.objects.all().filter(subscriber=user, book__name=book)[0].delete()

    return render(request, 'account/account.html', {'user': user, 'orders': orders, 'error': error})
