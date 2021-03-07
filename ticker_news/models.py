from django.db import models
from django.utils import timezone


class TickerNews(models.Model):
    symbol = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    source = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)

