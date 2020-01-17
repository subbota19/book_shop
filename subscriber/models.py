from django.db import models
from online_users.models import OnlineUserActivity
from subbota_traning import settings
from django.core.cache import cache
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


# Create your models here.
class Subscribers(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True)
    all_buys = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100000)], default=0)
    cache = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100000)], default=0)

    def last_seen(self):
        return cache.get(self.user_name)

    def check_user_status(self):
        now = datetime.datetime.now()
        try:
            return not now > self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)
        except TypeError:
            return False

    def save(self, *args, **kwargs):
        if self.all_buys > 200:
            self.discount = 0.05
        if self.all_buys > 500:
            self.discount = 0.10
        if self.all_buys > 1000:
            self.discount = 0.15
        if self.all_buys > 2000:
            self.discount = 0.20
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
