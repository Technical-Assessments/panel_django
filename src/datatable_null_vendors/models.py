from django.db import models

# Create your models here.


class DataTable(models.Model):
    id = models.IntegerField(primary_key=True)
    vendorid = models.FloatField(null=True)
    tpep_pickup_datetime = models.DateTimeField()
    trip_distance = models.FloatField()
    payment_type = models.FloatField(null=True)
    

class Yellowtaxis(models.Model):
    id = models.IntegerField(primary_key=True)
    vendorid = models.FloatField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    tpep_pickup_datetime = models.DateTimeField(blank=True, null=True)
    tpep_dropoff_datetime = models.DateTimeField(blank=True, null=True)
    trip_duration_seconds = models.IntegerField(blank=True, null=True)
    trip_duration = models.CharField(max_length=5, blank=True, null=True)
    passenger_count = models.FloatField(blank=True, null=True)
    trip_distance = models.FloatField(blank=True, null=True)
    ratecodeid = models.FloatField(blank=True, null=True)
    store_and_fwd_flag = models.CharField(max_length=1, blank=True, null=True)
    pulocationid = models.FloatField(blank=True, null=True)
    dolocationid = models.FloatField(blank=True, null=True)
    payment_type = models.FloatField(blank=True, null=True)
    fare_amount = models.FloatField(blank=True, null=True)
    extra = models.FloatField(blank=True, null=True)
    mta_tax = models.FloatField(blank=True, null=True)
    tip_amount = models.FloatField(blank=True, null=True)
    tolls_amount = models.FloatField(blank=True, null=True)
    improvement_surcharge = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    congestion_surcharge = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'yellowtaxis'
