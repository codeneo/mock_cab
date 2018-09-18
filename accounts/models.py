from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Account(AbstractUser):
    ACCOUNTS = (
        ('rider', 'rider'),
        ('driver', 'driver'),
    )

    account_type = models.CharField(max_length=20, choices=ACCOUNTS, default='rider')

    def __str__(self):
        return "Account: (id={}, user={}, account_type={})" \
                .format(self.id, self.username, self.account_type)

