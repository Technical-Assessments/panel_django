from django.db import models

# Create your models here.
class DataTable(models.Model):
    vendorid = models.FloatField()
    tpep_pickup_datetime = models.DateTimeField()
    trip_distance = models.FloatField()
    payment_type = models.FloatField()