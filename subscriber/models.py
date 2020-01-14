from django.db import models
from online_users.models import OnlineUserActivity
from subbota_traning import settings
from django.core.cache import cache
import datetime


# Create your models here.
class Subscribers(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True)
    is_online = models.BooleanField(default=False)

    def last_seen(self):
        return cache.get(self.user_name)

    def check_user_status(self):
        now = datetime.datetime.now()
        try:
            return not now > self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)
        except TypeError:
            return False

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
