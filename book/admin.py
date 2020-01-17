from django.contrib import admin
from book.models import Books, Comments
import numpy


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author_name', 'image', 'quantity', 'price', 'rating', 'discount', 'total_price']
    list_filter = ['name', 'price']  # block filter
    search_fields = ['name', 'price', 'author__name']

    @staticmethod
    def rating(obj):
        return numpy.average([x.rating for x in obj.comments_set.all()])
    @staticmethod
    def author_name(obj):
        return ','.join(x.name for x in obj.author.all())


class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'book']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'subscriber', 'book', 'description', 'rating']


admin.site.register(Books, BookAdmin)
admin.site.register(Books.author.through, BookAuthorAdmin)
admin.site.register(Comments, CommentAdmin)
