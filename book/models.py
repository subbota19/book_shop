from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from author.models import Authors
from subscriber.models import Subscribers


# Create your models here.

# class CalculateTotalPrice(models.Manager): def get_queryset(self): return super().get_queryset().extra(select={
# 'total_discount': 'price' if 'discount' == 0 else 'discount*price'})

class Books(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True, default=None)
    year = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2020)])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    image = models.ImageField(upload_to='books_image/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    total_price = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True)

    author = models.ManyToManyField(Authors, through='BooksAuthor')
    comment = models.ManyToManyField(Subscribers, through='Comments')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def save(self, *args, **kwargs):
        self.total_price = self.price - self.price * self.discount
        super().save(*args, **kwargs)


class BooksAuthor(models.Model):
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'LinkBooksAuthor'
        verbose_name_plural = 'LinkBooksAuthor'


class Comments(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    description = models.TextField(blank=True, null=True, default=None)
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.subscriber.user_name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
