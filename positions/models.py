from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from portfolios.models import Portfolio


class Position(models.Model):
    symbol = models.CharField(max_length=50)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    volumn = models.FloatField()
    buy_price = models.FloatField()
    budget = models.FloatField()
    sell_price = models.FloatField()
    expected_profit = models.FloatField()
    actual_profit = models.FloatField()
    position_tags = ArrayField(models.CharField(max_length=10))
    created_date = models.DateTimeField(default=timezone.now)
    sold_date = models.DateTimeField()

