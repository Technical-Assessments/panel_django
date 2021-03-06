from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from datatable_null_vendors.models import DataTable
# Create your views here.


def home_view(*args, **kwargs):

    return HttpResponse("<h1> Hello </h1>")


def panel(request, *args, **kwargs):
    rows = DataTable.objects.all()
    paginator = Paginator(rows, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "base.html", {'page_obj': page_obj})

'''
   context = {
        'id': obj.id,
        'vendorid': obj.vendorid,
        'tpep_pickup_datetime': obj.tpep_pickup_datetime,
        'trip_distance': obj.trip_distance,
        'payment_type': obj.payment_type
    }
'''