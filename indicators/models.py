from django.db import models


class Indicator(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
