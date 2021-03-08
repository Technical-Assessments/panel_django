from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import F
from rest_framework import generics

from datatable_null_vendors.models import DataTable
from rest_framework import viewsets
from datatable_null_vendors.serializers import TripSerializer
from datatable_null_vendors.models import Yellowtaxis

# Create your views here.


def home_view(request, *args, **kwargs):

    return render(request, "home.html")


def panel(request, *args, **kwargs):

    rows = DataTable.objects.all()
    paginator = Paginator(rows, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "base.html", {'page_obj': page_obj})


def edit(request, id):
    row = DataTable.objects.get(id=id)
    return render(request, 'edit.html', {'row': row})


class TripViewSet(
    #generics.ListAPIView
    viewsets.ReadOnlyModelViewSet
):
    queryset = Yellowtaxis.objects.all().order_by('vendorid')
    serializer_class = TripSerializer

'''    def get_queryset(self):
        queryset = Yellowtaxis.objects.all()
        vendor = self.request.query_params.get('vendorid', None)
        if vendor is not None:
            queryset = queryset.filter(vendorid__username=vendor)
        return queryset
'''

#F('trip_distance').desc(nulls_last=True)