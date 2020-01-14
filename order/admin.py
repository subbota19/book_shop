from django.contrib import admin
from order.models import Orders, Status


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'subscriber', 'status_availability', 'status', 'book_name', 'quantity', 'total_book_price',
                    'created',
                    'updated']
    search_fields = ['subscriber__user_name', 'book__total_price']

    @staticmethod
    def book_name(obj):
        return obj.book.name

    @staticmethod
    def total_book_price(obj):
        return obj.book.total_price * obj.quantity

    @staticmethod
    def subscriber(obj):
        return obj.subscriber.user_name


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']


admin.site.register(Status, StatusAdmin)
admin.site.register(Orders, OrderAdmin)
