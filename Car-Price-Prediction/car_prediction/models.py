from django.db import models

# Create your models here.
from django.db import models

class CarInput(models.Model):
    mileage = models.FloatField()
    num_owners = models.IntegerField()
    year = models.IntegerField()
    starting_bid = models.FloatField()
