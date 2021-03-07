from django.db import models
from django.utils import timezone


class Indicator(models.Model):
    custom_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    parmas = models.JSONField()
    parmas = models.JSONField()
    created_time = models.DateTimeField(default=timezone.now)
    updated_time = models.DateTimeField(default=timezone.now)
