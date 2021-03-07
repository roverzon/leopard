from django.db import models


class OpenClose(models.Model):
    tid = models.CharField(max_length=100, unique=True)
    tdate = models.DateTimeField()
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volumne = models.BigIntegerField()
    afterHours = models.FloatField()
    preMarket = models.FloatField()


