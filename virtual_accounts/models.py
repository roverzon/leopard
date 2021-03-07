from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from bank_accounts.models import BankAccount


class VirtualAccount(models.Model):
    name = models.CharField(max_length=100, blank=True, default='Unnamed_0')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    tags = ArrayField(models.CharField(max_length=100))
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
