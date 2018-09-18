from django.db import models
from accounts.models import Account
from cabs.models import Cab

# # Create your models here.
class Trip(models.Model):
    latitude_start = models.IntegerField(null=True, blank=True)
    longitude_start = models.IntegerField(null=True, blank=True)
    latitude_end = models.IntegerField(null=True, blank=True)
    longitude_end = models.IntegerField(null=True, blank=True)
    journey_date = models.DateTimeField(auto_now_add=True)
    vehicle = models.ForeignKey(Cab, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return "Trip: (id={}, vehicle={}, passenger={})" \
                .format(self.id, self.vehicle, self.passenger)