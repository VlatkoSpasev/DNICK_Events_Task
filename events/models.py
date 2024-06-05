from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    poster = models.ImageField(upload_to='events/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bands = models.CharField(max_length=255, null=True, blank=True)
    open_air = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Bands(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    year = models.IntegerField()
    n_events = models.IntegerField()

    def __str__(self):
        return self.name

class BandEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    band = models.ForeignKey(Bands, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.name
