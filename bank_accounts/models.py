from django.db import models
from django.conf import settings
from django.utils import timezone


class BankAccount(models.Model):
    name = models.CharField(max_length=255, blank=False)
    account_number = models.BigIntegerField()
    amount = models.BigIntegerField(default=100000)
    bank_name = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
