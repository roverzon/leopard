from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from overviews.models import Overview
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from virtual_accounts.models import VirtualAccount


class WatchList(models.Model):
    name = models.CharField(max_length=100, blank=True, default='Unnamed_0')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    tags = ArrayField(models.CharField(max_length=100))
    symbol_cnt = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)


class WatchListToSymbol(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
