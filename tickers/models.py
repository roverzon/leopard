from django.db import models
from django.utils import timezone


class Ticker(models.Model):
    symbol = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    locale = models.CharField(max_length=100)
    active = models.BooleanField()
    currency_name = models.CharField(max_length=100)
    cik = models.CharField(max_length=100)
    composite_figi = models.CharField(max_length=100)
    share_class_figi = models.CharField(max_length=100)
    last_updated_utc = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
