from django.contrib import admin
from subscriber.models import Subscribers


# Register your models here.
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'email', 'is_online', 'discount', 'basket', 'total_price']
    list_filter = ['user_name', 'id', 'email']  # block filter
    search_fields = ['user_name', 'email']

    @staticmethod
    def basket(obj):
        return [x.book for x in obj.orders_set.all()]

    @staticmethod
    def total_price(obj):
        total = sum([x.book.total_price * x.quantity for x in obj.orders_set.all()])
        return total - total * obj.discount


admin.site.register(Subscribers, SubscribersAdmin)
