from django.db import models
from book.models import Books
from subscriber.models import Subscribers
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Orders(models.Model):
    description = models.TextField(blank=True, null=True, default=None)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status_availability = models.BooleanField(default=False)

    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

    def __str__(self):
        return self.book.name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):
        if self.book.quantity >= self.quantity:
            self.status_availability = True
            self.book.quantity -= self.quantity
            super(Books, self.book).save(*args, **kwargs)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.book.quantity += self.quantity
        if self.book.quantity >= self.quantity:
            self.status_availability = True
        super(Books, self.book).save(*args, **kwargs)
        super().delete(*args, **kwargs)


class Status(models.Model):
    title = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
