from django.contrib import admin
from author.models import Authors


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'book_name', 'book_quantity', 'image']
    list_filter = ['name']
    search_fields = ['name']

    @staticmethod
    def book_name(obj):
        return '\n'.join(x.name for x in obj.books_set.all())

    @staticmethod
    def book_quantity(obj):
        return sum([x.quantity for x in obj.books_set.all()])


admin.site.register(Authors, AuthorAdmin)
