from django.db import models

# Create your models here.
class DataTable(models.Model):
    id = models.IntegerField(primary_key=True)
    vendorid = models.FloatField(null=True)
    tpep_pickup_datetime = models.DateTimeField()
    trip_distance = models.FloatField()
    payment_type = models.FloatField(null=True)