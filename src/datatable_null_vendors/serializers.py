from rest_framework import serializers

from datatable_null_vendors.models import Yellowtaxis


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Yellowtaxis
        fields = ('vendorid', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'trip_distance')
