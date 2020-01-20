from subscriber.models import Subscribers
from order.models import Orders, Status


def logic_account_delete_book(request_POST, user):
    for book in request_POST.getlist('book'):
        Orders.objects.all().filter(subscriber=user, book__name=book)[0].delete()


def logic_account_order_book(request_POST, user, status, error):
    for book in request_POST.getlist('book'):
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
    return error


def logic_account(user_name):
    user = Subscribers.objects.all().get(user_name=user_name)
    orders = Orders.objects.all().filter(subscriber=user)
    status = Status.objects.all().get(title='Выполнен')
    error = ''
    return {'user': user, 'orders': orders, 'error': error, 'status': status}
