from django.db import models
from accounts.models import Account

# Create your models here.
class Cab(models.Model):
    STATUS = (
        ('online', 'online'),
        ('waiting', 'waiting'),
        ('on_trip', 'on_trip'),
        ('offline', 'offline'),
        ('defunct', 'defunct'),
    )
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='online')
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return "Cab: (id={}, latitude={}, longitude={}, status={})" \
                .format(self.id, self.latitude, self.longitude, self.status)